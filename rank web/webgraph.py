import random

class WebGraph:
    """
    Represents a web of pages with links.
    """

    def __init__(self, pages):

        #Initialize the web graph with a dictionary of pages. Each page has a set of outgoing links.

        self.pages = {page: set() for page in pages}

    def add_link(self, source, target):

        #Adds a hyperlink from source to target.

        if source in self.pages and target in self.pages:
            self.pages[source].add(target)

    def get_links(self, page):

        #Returns the set of pages that the given page links to.

        return self.pages.get(page, set())

    def get_pages(self):

        #Returns all pages in the web graph.

        return set(self.pages.keys())

    def random_walk(self, start_page, steps=10):

        #Performs a random walk from a start page for a given number of steps.

        page = start_page
        path = [page]

        for _ in range(steps):
            links = self.get_links(page)
            if links:
                page = random.choice(list(links))
            else:
                page = random.choice(list(self.pages.keys()))  # Restart from a random page
            path.append(page)

        return path
