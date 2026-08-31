import json
from pprint import pprint
import requests
from bs4 import BeautifulSoup

URL = "https://minecraft.wiki/api.php"

"""
Overall fetches MOST data but not all, 
Here are the main Category's that did not get anything:
- Trading
- Brewing
- Enchanting
- Biomes

ALSO, need to organize the keys by alphabetic order in json file next time!
"""






def get_topics(category):
    '''


    :param category:
    :return: A list of all categories available in the main category
    '''
    session = requests.Session()

    # Base parameters for fetching all categories
    params = {
        "action": "query",
        "format": "json",
        "list": "categorymembers",
        "cmtitle": f"Category:{category}",
        "cmtype": "page",
        "cmlimit": "max"  # Fetches 500 categories per request
    }
    all_categories = []
    response = session.get(url=URL, params=params)
    data = response.json()
    pprint(data.keys())
    print(f"--------------- MAIN CATEGORY: {category.upper()} ---------------")

    categories_batch = data.get("query", {}).get("categorymembers", [])
    for cat in categories_batch:
        all_categories.append(cat["title"])
    #pprint(all_categories)
    return all_categories

def web_scrape(topic):
    """

    :param topic:
    :return: end (clean text description of topic)
    """
    end = ""
    PARAMS = {
        "action": "parse",
        "page": topic,
        "format": "json",
        "prop": "text"
    }
    # Ensure this is highly descriptive to pass automated wiki bot filtering
    headers = {
        "User-Agent": "MinecraftSearchEngineProject/1.0 (contact: dannywarr911@gmail.com)"
    }
    try:
        # 1. Fetch data from endpoint
        response = requests.get(url=URL, params=PARAMS, headers=headers)
        # 3. Attempt safe decoding
        data = response.json()
        # 4. Extract data on successful parsing
        page_html = data["parse"]["text"]["*"]
        soup = BeautifulSoup(page_html, "html.parser")
        print(f"Success! {topic} Content fetched:")
        text = soup.find_all('p')

        for p in text:
            clean_text = p.get_text().strip()
            if clean_text != "" and not clean_text.endswith(":"):
                end+=p.text

    except requests.exceptions.JSONDecodeError:
        print("\n[!] CRASH PREVENTED: Server did not return a readable JSON string.")
        print("This means the wiki firewall or Cloudflare intercepted your code request.")
        print("\n--- BEGINNING OF RETURNED HTML TEXT ---")
        print(response.text[:800])  # Inspect the actual server complaint output
        print("--- END OF RETURNED HTML TEXT ---\n")

    except Exception as e:
        print(f"An unexpected networking issue occurred: {e}")

    return end


def make_dict(topics):
    """

    :param topics:
    :return: topic_dict (This is a dictionary form of output. Key=Topic, Value=Description)
    """
    topic_dict = {}
    for topic in topics:
        topic_desc = web_scrape(topic)
        if topic_desc:
            topic_dict[topic] = topic_desc
    return topic_dict

def save_json(dictionary, filename):
    '''

    :param dictionary:
    :param filename:
    :return: Saves to a json file neatly
    '''
    with open(filename, "w") as f:
        json.dump(dictionary, f, indent=4,)




def pipeline():
    '''
        Runs FUll pipeline:
        -Iterates through every main category
        -gets topics for category
        - adds dict with key being the topic and values its description to topic_dict
        -saves that huge dictionary to json for later use!

    '''
    main_categories = ["Trading", "Brewing", "Enchanting",
                       "Mobs", "Blocks", "Items",
                       "Biomes", "Effects", "Crafting",
                       "Smelting", "Smithing", "Structures",
                       "Redstone", "History"]
    topic_dict = {}
    for category in main_categories:
        topics = get_topics(category)
        topic_dict.update(make_dict(topics))

    save_json(topic_dict, f"topic_dict.json")

pipeline()








