import json
import pprint as pp
import string

"""
1. make description -> set of words, but lowercase everything and clean it up

"""
file_name = "topic_dict.json"
with open(file_name) as json_file:
    data = json.load(json_file)


def is_english(text):
    # Checks if the string can be cleanly converted to standard ASCII
    try:
        text.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False

#pp.pprint(data)

def reverse_index(data):

    new_dict = {}


    for topic in data:
        value = data[topic]
        clean = value.lower()
        clean = value.translate(str.maketrans('', '', string.punctuation))
        description_set = set()
        for word in clean.split():
            if word.isalpha() and is_english(word):
                description_set.add(word)
        new_dict[topic] = list(description_set)


    reversed_dict = {}
    '''
    going through every word in the list, for every word that is new, add that as a key into reversed_dict,
    if topic has that word in it, add topic to a set of topics attached to that word
    
    '''

    for topic in new_dict:
        value = new_dict[topic]
        for word in value:

            if word not in reversed_dict:

                reversed_dict[word] = []

    for topic in new_dict:
        value = new_dict[topic]
        for word in value:
            reversed_dict[word].append(topic)

    pp.pprint(reversed_dict)

    pp.pprint(reversed_dict["explosion"])



reverse_index(data)