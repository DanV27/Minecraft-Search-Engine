"""
Where we will make search function to look through the reversed index dictionary we made!
"""
import json
from reverse import reverse_index
import pprint as pp

file_name = "topic_dict.json"
with open(file_name) as json_file:
    data = json.load(json_file)

dictionary = reverse_index(data)


print("MINECRAFT SEARCH ENGINE")
input_search = input("What would you like to search?: ")

if input_search in dictionary:
    print(f"The topics you are looking for: {dictionary[input_search]}")

