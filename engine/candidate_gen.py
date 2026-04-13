from collections import defaultdict


class CandidateGenerator:

    def __init__(self, user_repo, content_repo, interaction_repo):
        self.user_repo = user_repo
        self.content_repo = content_repo
        self.interaction_repo = interaction_repo

    def _load_user_data(self):
        user_data = defaultdict(list)
        for i in self.interaction_repo.get_all():
            user_data[i.user_id].append(i.content_id)
        return user_data

    def _load_item_data(self):
        item_data = {}
        for c in self.content_repo.all():
            item_data[c.id] = c.category
        return item_data

    def hybrid_candidates(self, user_id):
        user_data = self._load_user_data()

        # cold start
        if user_id not in user_data:
            return self.popularity_candidates(user_data)

        return self.popularity_candidates(user_data)

    def popularity_candidates(self, user_data):
        count = defaultdict(int)
        for items in user_data.values():
            for item in items:
                count[item] += 1

        return sorted(count, key=count.get, reverse=True)