import numpy as np
from collections import defaultdict
from engine.candidate_gen import CandidateGenerator
from engine.scorer import RecommendationScorer
from engine.similarity import SimilarityCalculator


class RecommendationOrchestrator:

    def __init__(self, user_repo, content_repo, interaction_repo):
        self.user_repo = user_repo
        self.content_repo = content_repo
        self.interaction_repo = interaction_repo

        self.candidate_gen = CandidateGenerator(user_repo, content_repo, interaction_repo)
        self.similarity = SimilarityCalculator()

        self.scorer = RecommendationScorer()
        self.cache = {}

    # 🔥 Build user-item matrix
    def build_matrix(self):
        users = self.user_repo.all()
        contents = self.content_repo.all()
        interactions = self.interaction_repo.get_all()

        user_ids = [u.id for u in users]
        item_ids = [c.id for c in contents]

        user_index = {u: i for i, u in enumerate(user_ids)}
        item_index = {c: i for i, c in enumerate(item_ids)}

        matrix = np.zeros((len(user_ids), len(item_ids)))

        for inter in interactions:
            if inter.user_id in user_index and inter.content_id in item_index:
                matrix[user_index[inter.user_id]][item_index[inter.content_id]] = inter.rating or 1

        return matrix, user_index, item_index

    # 🔥 Collaborative Filtering Score
    def collaborative_score(self, user_id, item_id, sim_matrix, user_index, item_index, matrix):
        if user_id not in user_index or item_id not in item_index:
            return 0

        u_idx = user_index[user_id]
        i_idx = item_index[item_id]

        similarities = sim_matrix[u_idx]
        scores = matrix[:, i_idx]

        return np.dot(similarities, scores)

    # 🔥 Content-Based Score
    def content_score(self, item_id, user_items, item_data):
        item_tags = set(item_data.get(item_id, []))
        score = 0

        for i in user_items:
            tags = set(item_data.get(i, []))
            if tags:
                score += len(item_tags & tags) / len(item_tags | tags)

        return score

    def get_recommendations(self, user_id, limit=5):

        if user_id in self.cache:
            return self.cache[user_id]

        user_data = self.candidate_gen._load_user_data()
        item_data = self.candidate_gen._load_item_data()

        candidates = self.candidate_gen.hybrid_candidates(user_id)

        # Cold start
        if user_id not in user_data:
            results = [{"item": c, "score": 1.0, "reason": "popular"} for c in candidates[:limit]]
            self.cache[user_id] = results
            return results

        # Build ML matrix
        matrix, user_index, item_index = self.build_matrix()
        sim_matrix = self.similarity.user_similarity(matrix)

        user_items = user_data[user_id]

        results = []

        for item in candidates:
            collab = self.collaborative_score(user_id, item, sim_matrix, user_index, item_index, matrix)
            content = self.content_score(item, user_items, item_data)
            popularity = sum(item in items for items in user_data.values())

            final_score = 0.5 * collab + 0.3 * content + 0.2 * popularity

            results.append({
                "item": item,
                "score": float(final_score),
                "reason": "hybrid ML"
            })

        results.sort(key=lambda x: x["score"], reverse=True)

        self.cache[user_id] = results[:limit]
        return self.cache[user_id]