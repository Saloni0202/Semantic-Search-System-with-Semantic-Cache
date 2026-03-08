import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class SemanticCache:

    def __init__(self, threshold=0.85):

        self.cache = []
        self.threshold = threshold
        self.hit_count = 0
        self.miss_count = 0


    def lookup(self, query_embedding):

        for entry in self.cache:

            score = cosine_similarity(
                [query_embedding],
                [entry["embedding"]]
            )[0][0]

            if score > self.threshold:

                self.hit_count += 1
                return True, entry, score

        self.miss_count += 1
        return False, None, None


    def add(self, query, embedding, result, cluster):

        self.cache.append({
            "query": query,
            "embedding": embedding,
            "result": result,
            "cluster": cluster
        })


    def stats(self):

        total = len(self.cache)

        total_requests = self.hit_count + self.miss_count

        hit_rate = self.hit_count / total_requests if total_requests else 0

        return {
            "total_entries": total,
            "hit_count": self.hit_count,
            "miss_count": self.miss_count,
            "hit_rate": hit_rate
        }


    def clear(self):

        self.cache = []
        self.hit_count = 0
        self.miss_count = 0