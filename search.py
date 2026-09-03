"""
Where we will make search function to look through the reversed index dictionary we made!
"""
import json
from reverse import reverse_index
import pprint as pp

file_name = "topic_dict.json"
with open(file_name) as json_file:
    data = json.load(json_file)


def basic_search(data):
    """

    :param data:
    :return: Printed List of related topics
    """

    dictionary = reverse_index(data)

    found = False
    print("MINECRAFT SEARCH ENGINE")

    input_search = input("What would you like to search?: ")
    while found == False:
        if input_search in dictionary:
            pp.pprint(f"The topics you are looking for: {dictionary[input_search]}")
            print("All done!")
            found = True
        else:
            print("Nothing found")
            input_search = input("What would you like to search?: ")

basic_search(data)