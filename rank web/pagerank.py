import numpy as np

class PageRank:
    """
    Computes PageRank scores for a set of web pages.
    """

    def __init__(self, webgraph, damping_factor=0.85, tolerance=1e-6):
        self.webgraph = webgraph
        self.damping_factor = damping_factor
        self.tolerance = tolerance
        self.pages = list(webgraph.get_pages())
        self.n = len(self.pages)
        self.page_indices = {page: i for i, page in enumerate(self.pages)}

    def transition_matrix(self):
        """
        Constructs the transition probability matrix.
        """
        matrix = np.zeros((self.n, self.n))

        for i, page in enumerate(self.pages):
            links = self.webgraph.get_links(page)
            if links:
                for link in links:
                    j = self.page_indices[link]
                    matrix[j][i] = 1 / len(links)
            else:
                # If no outgoing links, assume equal probability to all pages
                matrix[:, i] = 1 / self.n

        return matrix

    def compute_pagerank(self, max_iterations=100):
        """
        Computes PageRank scores using power iteration.
        """
        M = self.transition_matrix()
        rank = np.ones(self.n) / self.n  # Initialize ranks uniformly
        teleport = np.ones(self.n) / self.n

        for _ in range(max_iterations):
            new_rank = self.damping_factor * np.dot(M, rank) + (1 - self.damping_factor) * teleport
            if np.linalg.norm(new_rank - rank, ord=1) < self.tolerance:
                break
            rank = new_rank

        return {self.pages[i]: rank[i] for i in range(self.n)}
