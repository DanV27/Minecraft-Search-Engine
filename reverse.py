import json
import pprint as pp
import string

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

def index_count(data):

    """
    FUNCTION index_count(data)
    - This function takes in data from a json file
    - iterates through every topic's description and returns a  nested dictionary with every word and its topics
    and how many times that topic has that word in its description


    :param data:
    :return: reversed_dict
    """
    reversed_dict = {}

    new_dict = {}
    for topic in data:
        value = data[topic]
        clean = value.lower()
        clean = clean.translate(str.maketrans('', '', string.punctuation))
        #we cleaned the description
        description_list = []
        for word in clean.split():
            if word.isalpha() and is_english(word):
                description_list.append(word)
                #only added english words
        new_dict[topic] = list(description_list)
        # now new_dict is topic: description




    for topic in new_dict:
        for word in new_dict[topic]:
            # We iterate through every word in every topics description
            if word not in reversed_dict:
                # if word not in the new reversed_dict
                reversed_dict[word] = {} # add an empty dictionary
            if topic not in reversed_dict[word]: # if topic inst in that words dictionary
                reversed_dict[word][topic] = 0 # add the topic and a 0 to it
            reversed_dict[word][topic] += 1 # add 1 to the counter for how many times the topic has this word in it


    #here we are just filtering out dicitonarys that are empty, so words that wont matter
    for key in list(reversed_dict.keys()):
        if not reversed_dict[key]:
            del reversed_dict[key]


    return(reversed_dict)








