from data.database import SessionLocal
from data.repositories import UserRepository, ContentRepository, InteractionRepository
from engine.orchestrator import RecommendationOrchestrator
from engine.evaluator import RecommendationEvaluator


def run_evaluation():
    db = SessionLocal()

    user_repo = UserRepository(db)
    content_repo = ContentRepository(db)
    interaction_repo = InteractionRepository(db)

    orchestrator = RecommendationOrchestrator(user_repo, content_repo, interaction_repo)
    evaluator = RecommendationEvaluator()

    users = user_repo.all()
    results = []

    for user in users:
        recs = orchestrator.get_recommendations(user.id)
        rec_ids = [r["item"] for r in recs]

        interactions = user_repo.get_interactions(user.id)
        relevant = [i.content_id for i in interactions]

        metrics = evaluator.evaluate(rec_ids, relevant, k=5)
        results.append(metrics)

    avg = {
        "precision@5": sum(r["precision@5"] for r in results) / len(results),
        "recall@5": sum(r["recall@5"] for r in results) / len(results),
        "ndcg@5": sum(r["ndcg@5"] for r in results) / len(results),
    }

    print("\n=== EVALUATION REPORT ===")
    print(avg)


if __name__ == "__main__":
    run_evaluation()