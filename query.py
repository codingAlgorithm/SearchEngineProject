import json


class Query:
    def __init__(self, keywords, yourfile):
        self.keywords = keywords
        self.yourfile = yourfile

    def processing(self):
        print "start query processing"
        # write you query logic here
        with open(self.yourfile) as data_file:
            index = json.load(data_file)

        result = []
        for keyword in self.keywords:
            if keyword in index.keys():
                urls = index[keyword]
                for url in urls:
                    if url not in result:
                        result.append(url)
        return result


# def main():
#     keywords = raw_input("give me your search keyword please: ")
#     keywords = keywords.split(" ")
#     print ("keywords: " + str(keywords))
#     query = Query(keywords, 'inverted_index.txt')
#     print query.processing()
#
#
# if __name__ == "__main__":
#     main()
