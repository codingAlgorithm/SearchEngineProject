import json

class Indexer():
    def __init__(self, file_address):
        self.file_address = file_address

    def build(self):
        data_file = open(self.file_address);
        data = json.load(data_file)
        records = data["records"]
        result = {}
        for record in records:
            url = record["url"]
            word_list = record["content"]
            for word in word_list:
                word = word.lower()
                if word not in result.keys():
                    result[word] = [url]
                else:
                    if url not in result[word]:
                        result[word].append(url)
        outfile = open('inverted_index.txt', 'w')
        json.dump(result, outfile, indent=4, encoding='ascii')

# def main():
#     indexer = Indexer("raw_index.txt")
#     indexer.build()
#
# if __name__ == "__main__":
#     main()






#
# value = data.values()
# list = value[0]
# nolist = list[0]
# content = nolist[u'content']
# url = nolist[u'url']
# listurl = [url]
#
#
#
# def create_index(data):
#     result = {}
#     for key in content:
#         result[key] = key
#     return result
# print create_index(content)
#
#
#
# # for key in data.keys():
# #     value = data[key]
# #     print key, value
#
#
# # class Indexer():
# #     def __init__(self):
#
# #
# # map = {"dyy": 12, "wz": 10, "sdkhf":13}
# #
# # for key in map.keys():
# #     value = map[key]
# #     print key, value
# #
# # print map["dyy"]
# # print map.keys()