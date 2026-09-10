"""
Where we will make search function to look through the reversed index dictionary we made!
"""
import json
import pprint as pp

file_name = "index.json"
with open(file_name) as json_file:
    data = json.load(json_file)

file_name2 = "topic_dict.json"
with open(file_name2) as json_file:
    topic_dict = json.load(json_file)

def basic_search(data):

    found = False

    search = input("What would you like to search?: ")

    while found == False:
        if search in data:

            sorted_data = dict(sorted(data[search].items(), key=lambda item: item[1], reverse=True))
            list_of_topics = []
            for key in sorted_data:
                #here we just make the dictionary into a list of only the topics
                list_of_topics.append(key)

            print(f"The topics you are looking for in order by relevance:")
            found = True
            pp.pprint(list_of_topics)
            print("Description most relevant topic: ")

            desc = topic_dict[list_of_topics[0]]
            print(desc)

        else:
            print("Nothing found")
            search = input("What would you like to search?: ")



basic_search(data)


