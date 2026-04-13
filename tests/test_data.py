from data.database import SessionLocal
from data.repositories import UserRepository, ContentRepository

def test_users_exist():
    db = SessionLocal()
    repo = UserRepository(db)
    users = repo.all()
    assert len(users) >= 10


def test_content_exist():
    db = SessionLocal()
    repo = ContentRepository(db)
    content = repo.all()
    assert len(content) >= 20