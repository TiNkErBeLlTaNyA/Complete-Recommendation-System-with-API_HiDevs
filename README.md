# Complete Recommendation System with API

## Project Overview

A production-ready hybrid recommendation system built using FastAPI, SQLite, and machine learning techniques. The system delivers personalized recommendations using collaborative, content-based, and popularity-based strategies.

---

##  Features

* Hybrid ML Recommendation Engine
* Collaborative + Content-Based + Popularity Filtering
* Cold Start Handling
* Explainable Recommendations
* FastAPI REST API
* Interactive Dashboard UI
* Evaluation Metrics (Precision@5, Recall@5, NDCG@5)
* Request Logging & Caching

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

##  API Endpoints

* **GET /recommend/{user_id}** → Get recommendations
* **POST /feedback** → Record feedback
* **GET /metrics** → System statistics
* **GET /health** → Health check
* **GET /ui** → Dashboard UI

---

##  Recommendation Logic

Hybrid scoring:

```
0.5 × collaborative + 0.3 × content + 0.2 × popularity
```

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

---

##  Demo Video

[▶Watch Demo Video](https://youtu.be/YOUR_VIDEO_ID)

---

##  Highlights

✔ Personalized recommendations
✔ Cold-start handling
✔ Explainable results
✔ API + UI integration
✔ Production-ready architecture

---

## Conclusion

This project builds a complete recommendation system that combines machine learning techniques with a practical API and database setup to deliver personalized results. By using a hybrid approach of collaborative, content-based, and popularity-based methods, the system is able to handle real-world challenges like cold-start users while providing meaningful recommendations with clear explanations. Overall, it demonstrates a solid understanding of both recommendation algorithms and full-stack system design.

---
