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



def reverse_index(data):
    '''
    FUNCTION reverse_index(data)
    - This function takes in data from a json file
    - iterates through every topic's description, make the
      description in a set of words, lowercase, no punctuations,
      has characters, is english and adds them to new_dict{}
     -The function then iterates through every topic's strings in new_dict, checks if the word hasnt been added to the new reversed_dict{}
     - Then adds the word and empty list,
     -then  adds topic to its list

    :param data:
    :return: reversed_dict
    '''
    new_dict = {}
    for topic in data:
        value = data[topic]
        clean = value.lower()
        clean = clean.translate(str.maketrans('', '', string.punctuation))
        description_set = set()
        for word in clean.split():
            if word.isalpha() and is_english(word):
                description_set.add(word)
        new_dict[topic] = list(description_set)

    reversed_dict = {}

    for topic in new_dict:
        value = new_dict[topic]
        for word in value:

            if word not in reversed_dict:

                reversed_dict[word] = []
            else:
                reversed_dict[word].append(topic)

    #deleting any left over empty value lists.
    for key in list(reversed_dict.keys()):
        if not reversed_dict[key]:
            del reversed_dict[key]

    return reversed_dict
#pp.pprint(reverse_index(data))


def index_count(data):
    reversed_dict = {}

    new_dict = {}
    for topic in data:
        value = data[topic]
        clean = value.lower()
        clean = clean.translate(str.maketrans('', '', string.punctuation))
        description_list = []
        for word in clean.split():
            if word.isalpha() and is_english(word):
                description_list.append(word)
        new_dict[topic] = list(description_list)




    for topic in new_dict:

        for word in new_dict[topic]:
            if word not in reversed_dict:
                reversed_dict[word] = {}
            if topic not in reversed_dict[word]:
                reversed_dict[word][topic] = 0
            reversed_dict[word][topic] += 1



    for key in list(reversed_dict.keys()):
        if not reversed_dict[key]:
            del reversed_dict[key]


    return(reversed_dict)








