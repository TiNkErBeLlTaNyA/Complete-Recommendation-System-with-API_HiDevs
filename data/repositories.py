from .models import User, Content, Interaction


class UserRepository:
    def __init__(self, db):
        self.db = db

    def get(self, user_id):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_interactions(self, user_id):
        return self.db.query(Interaction).filter_by(user_id=user_id).all()

    def all(self):
        return self.db.query(User).all()


class ContentRepository:
    def __init__(self, db):
        self.db = db

    def all(self):
        return self.db.query(Content).all()

    def get(self, content_id):
        return self.db.query(Content).filter(Content.id == content_id).first()


class InteractionRepository:
    def __init__(self, db):
        self.db = db

    def add(self, interaction):
        self.db.add(interaction)
        self.db.commit()

    def get_all(self):
        return self.db.query(Interaction).all()