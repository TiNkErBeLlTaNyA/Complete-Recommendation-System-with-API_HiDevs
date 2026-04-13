from data.database import SessionLocal
from data.repositories import UserRepository, ContentRepository, InteractionRepository
from engine.orchestrator import RecommendationOrchestrator

def test_recommendations_return():
    db = SessionLocal()

    orchestrator = RecommendationOrchestrator(
        UserRepository(db),
        ContentRepository(db),
        InteractionRepository(db)
    )

    recs = orchestrator.get_recommendations(1)

    assert recs is not None
    assert len(recs) > 0


def test_cold_start():
    db = SessionLocal()

    orchestrator = RecommendationOrchestrator(
        UserRepository(db),
        ContentRepository(db),
        InteractionRepository(db)
    )

    recs = orchestrator.get_recommendations(999)  # new user
    assert len(recs) > 0