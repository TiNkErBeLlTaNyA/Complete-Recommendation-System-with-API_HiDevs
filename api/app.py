import time
import uuid
import logging
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from data.database import SessionLocal, engine, Base
from data.repositories import UserRepository, ContentRepository, InteractionRepository
from engine.orchestrator import RecommendationOrchestrator

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create DB
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Middleware for request ID + logging
@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start = time.time()

    response = await call_next(request)

    duration = time.time() - start
    logger.info(f"[{request_id}] {request.method} {request.url} - {duration:.4f}s")

    response.headers["X-Request-ID"] = request_id
    return response


@app.get("/")
def root():
    return {"message": "Recommendation API Running 🚀"}

@app.get("/ui", response_class=HTMLResponse)
def ui():
    with open("api/ui.html") as f:
        return f.read()

@app.get("/recommend/{user_id}")
def recommend(user_id: int, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    content_repo = ContentRepository(db)
    interaction_repo = InteractionRepository(db)

    orchestrator = RecommendationOrchestrator(
        user_repo, content_repo, interaction_repo
    )

    user = user_repo.get(user_id)

    recs = orchestrator.get_recommendations(user_id)

    return {
        "user_id": user_id,
        "results": recs,
        "note": "cold start user" if not user else "existing user"
    }


@app.post("/feedback")
def feedback(user_id: int, content_id: int, db: Session = Depends(get_db)):
    interaction_repo = InteractionRepository(db)

    from data.models import Interaction
    interaction = Interaction(
        user_id=user_id,
        content_id=content_id,
        type="click",
        rating=5
    )

    interaction_repo.add(interaction)

    return {"status": "feedback recorded"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/metrics")
def metrics(db: Session = Depends(get_db)):
    users = UserRepository(db).all()
    interactions = InteractionRepository(db).get_all()

    return {
        "total_users": len(users),
        "total_interactions": len(interactions)
    }