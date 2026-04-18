# Complete Recommendation System with API

## Project Overview

This project implements a hybrid recommendation system using FastAPI and SQLite.

The system combines three basic strategies:
- Collaborative filtering (based on user interactions)
- Content-based filtering (based on category)
- Popularity-based recommendations

It provides a simple API and UI to fetch and visualize recommendations.

---

##  Features

- Hybrid ML Recommendation Engine
- Cold start handling for new users
- Explainable recommendations (reason field)
- REST API built with FastAPI
- SQLite database
- Evaluation metrics (Precision@5, Recall@5, NDCG@5)
- Basic unit tests
- Simple dashboard UI

---

##  Architecture

User → API → Orchestrator → Candidate Generator → Scorer → Database → Response

---

##  Project Structure

```
├── data/
├── engine/
├── api/
├── scripts/
├── tests/
```

---

##  Setup Instructions

```bash
pip install -r requirements.txt
python -m scripts.seed_data
uvicorn api.app:app --reload
```

---

## Database Schema

The system uses a SQLite database with three tables:

users (id, name, interests, created_at)
content (id, title, category, difficulty, popularity)
interactions (user_id, content_id, type, rating, created_at)

Relationships:

Users interact with content through interactions

---

##  API Endpoints

* **GET /recommend/{user_id}** → Get recommendations

Example response (existing user):                             
{
  "user_id": 1,
  "results": [
    {
      "item": 6,
      "score": 3.45,
      "reason": "based on similar users"
    }
  ],
  "note": "existing user"
}

Example response (new user):  
{
  "user_id": 999,
  "results": [...],
  "note": "cold start user"
}

* **POST /feedback** → Record feedback
* **GET /metrics** → System statistics
- total users
- total interactions
* **GET /health** → Health check endpoint
* **GET /ui** → Dashboard UI

---

##  Recommendation Logic

The system follows a hybrid approach:

- Collaborative Filtering
- Finds items used by similar users
- Content-Based Filtering
- Recommends items with similar categories
- Popularity-Based Filtering
- Recommends frequently interacted items

These are combined using weighted scoring.

---

##  Evaluation

Run:

```bash
python -m scripts.evaluate
```

Metrics used:

* Precision@5
* Recall@5
* NDCG@5

Sample Results

* precision@5: 0.58  
* recall@5: 0.57  
* ndcg@5: 0.62  

These results indicate that the system provides reasonably accurate and well-ranked recommendations.

---

## Testing

Run:

```bash
pytest
```

Includes:
* API tests
* Data tests
* Recommendation engine tests

---

## UI

The project includes a simple dashboard:

- Displays recommendations
- Shows scores using a bar chart
- Displays total users and interactions

---

##  Demo Video

[▶Watch Demo Video](https://youtu.be/YOUR_VIDEO_ID)

---

## Conclusion

This project demonstrates a working hybrid recommendation system with API integration, basic evaluation, and a simple UI. It focuses on clarity, correctness, and modular design.

---
