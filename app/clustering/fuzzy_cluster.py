import hdbscan


class FuzzyCluster:

    def __init__(self):

        self.clusterer = hdbscan.HDBSCAN(
            min_cluster_size=30,
            prediction_data=True
        )

    def fit(self, embeddings):

        labels = self.clusterer.fit_predict(embeddings)

        probabilities = self.clusterer.probabilities_

        return labels, probabilities