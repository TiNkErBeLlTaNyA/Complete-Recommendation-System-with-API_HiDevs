import math


class RecommendationEvaluator:

    def precision_at_k(self, recs, relevant, k):
        return len(set(recs[:k]) & set(relevant)) / k if k else 0

    def recall_at_k(self, recs, relevant, k):
        if not relevant:
            return 0.0
        return len(set(recs[:k]) & set(relevant)) / len(relevant)

    def ndcg_at_k(self, recs, relevant, k):
        dcg = sum(
            1 / math.log2(i + 2)
            for i, item in enumerate(recs[:k])
            if item in relevant
        )

        ideal = sum(1 / math.log2(i + 2) for i in range(min(len(relevant), k)))
        return dcg / ideal if ideal else 0.0

    def evaluate(self, recs, relevant, k=5):
        return {
            "precision@5": self.precision_at_k(recs, relevant, k),
            "recall@5": self.recall_at_k(recs, relevant, k),
            "ndcg@5": self.ndcg_at_k(recs, relevant, k),
        }