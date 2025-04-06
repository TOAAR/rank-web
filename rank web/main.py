from webgraph import WebGraph
from pagerank import PageRank

def main():
    # Define a set of web pages
    pages = ["A", "B", "C", "D", "E"]
    web = WebGraph(pages)

    # Define links between pages
    web.add_link("A", "B")
    web.add_link("A", "C")
    web.add_link("B", "C")
    web.add_link("C", "A")
    web.add_link("D", "C")
    web.add_link("D", "E")
    web.add_link("E", "B")

    # Compute PageRank scores
    pagerank = PageRank(web)
    scores = pagerank.compute_pagerank()

    # Print the PageRank scores
    print("\nPageRank Scores:")
    for page, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        print(f"{page}: {score:.4f}")

if __name__ == "__main__":
    main()
