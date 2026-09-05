"""
Where we will make search function to look through the reversed index dictionary we made!
"""
import json
from reverse import index_count
import pprint as pp

file_name = "topic_dict.json"
with open(file_name) as json_file:
    data = json.load(json_file)


def basic_search(data):
    """

    :param data:
    :return: Printed List of related topics
    """

    dictionary = index_count(data)

    found = False
    print("MINECRAFT SEARCH ENGINE")

    input_search = input("What would you like to search?: ")
    while found == False:
        if input_search in dictionary:
            sorted_data = dict(sorted(dictionary[input_search].items(), key=lambda item: item[1], reverse=True))
            list_of_topics = []
            for key in sorted_data:
                list_of_topics.append(key)

            print(f"The topics you are looking for in order by relevance: \n{list_of_topics}")
            print("All done!")
            found = True
        else:
            print("Nothing found")
            input_search = input("What would you like to search?: ")

basic_search(data)