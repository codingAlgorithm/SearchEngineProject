# -*- coding: utf-8 -*-
import re
from Queue import Queue
import json
from bs4 import BeautifulSoup
import urllib2

# save all you crawled web page url and content to file in json format
stop_words = ["", " ", ",", ".", "?"]


class Crawler:
    def __init__(self, base_url, deep, pages):
        self.base_url = base_url
        self.deep = deep
        self.pages = pages

    def visible(self, element):
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
            return False
        return True

    def bfs(self):
        data = []

        q = Queue()
        q.put(self.base_url)
        i = 0
        while not q.empty():
            i += 1
            if i > self.pages:
                break

            url = q.get()
            print url
            content = self.get_content_of_page(url)
            links = self.get_links_in_page(url, content)

            record = {}
            record["url"] = url

            soup = BeautifulSoup(content, "html.parser")
            texts = soup.findAll(text=True)
            visible_texts = filter(self.visible, texts)
            final_texts = []
            for i in range(len(visible_texts)):
                if not visible_texts[i].strip() in stop_words:
                    pieces = visible_texts[i].strip().split(" ")
                    for piece in pieces:
                        if not piece in stop_words:
                            final_texts.append(piece)

        record["content"] = final_texts
        data.append(record)

        for link in links:
            q.put(link)

        final_data = {"records": data}
        print data
        outfile = open('raw_index.txt', 'w')
        json.dump(final_data, outfile, indent=4, encoding='ascii')

    def get_content_of_page(self, url):

        """
        Args:
            param1 (str): The url of web page

        Returns:
            Str: return content of this web page

        """
        try:
            return urllib2.urlopen(url).read()
        except urllib2.URLError:
            return ""

    def get_links_in_page(self, url, content):

        """
        Args:
            param1 (str): The content of web page

        Returns:
            List: return a list of url inside a web page

        """
        soup = BeautifulSoup(content, "html.parser")
        links = []
        for a in soup.findAll('a', href=True):
            links.append(url + a['href'])
        return links

    def start(self):
        print "start crawl web pages"
        self.bfs()
        print "end work"



# def main():
#     base = "http://www.wikipedia.org/wiki/Main_Page"
#     crawler = Crawler(base, 1, 1)
#     crawler.start()
#
# if __name__ == "__main__":
#     main()
