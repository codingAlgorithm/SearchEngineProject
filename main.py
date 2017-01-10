from crawler import Crawler
from indexer import Indexer
from query import Query

def main():
    #receive max Deep for bfs and max pages from keyboard
    deep = raw_input("what's max bfs deep you want to set up")
    max_pages = raw_input("what's max number of pages you want to set up")
    base_url = raw_input("what's baseURL of pages you want to set up")

    #start crawl web page
    crawler = Crawler(deep, max_pages, base_url)
    crawler.start()

    #start building index
    indexer = Indexer()
    indexer.build()

    #start processing query
    keywords = raw_input("give me your search keyword please")
    keywords = keywords.split(" ")
    query = Query(keywords)
    query.processing()


if __name__ == "__main__":
    main()
