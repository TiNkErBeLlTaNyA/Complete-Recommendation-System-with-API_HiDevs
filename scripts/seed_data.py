from data.database import SessionLocal, engine, Base
from data.models import User, Content, Interaction

Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Diverse interests
interests_list = ["AI", "ML", "Data Science", "Web Dev"]

# Users
for i in range(1, 11):
    db.add(User(
        id=i,
        name=f"User{i}",
        interests=interests_list[i % len(interests_list)]
    ))

# Diverse categories
categories = ["AI", "ML", "Data Science", "Web Dev"]

# Content
for i in range(1, 21):
    db.add(Content(
        id=i,
        title=f"Course{i}",
        category=categories[i % len(categories)],
        difficulty=["easy", "medium", "hard"][i % 3],
        popularity=20 - i  # reverse for variation
    ))

# Interactions (more realistic pattern)
for i in range(1, 11):
    for j in range(1, 6):  # each user interacts with 5 items
        db.add(Interaction(
            user_id=i,
            content_id=((i + j) % 20) + 1,
            type="view",
            rating=(j % 5) + 1
        ))

db.commit()
db.close()