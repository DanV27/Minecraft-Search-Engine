import json
from pprint import pprint
import requests
from bs4 import BeautifulSoup

URL = "https://minecraft.wiki/api.php"

def get_categories():
    session = requests.Session()

    # Base parameters for fetching all categories
    params = {
        "action": "query",
        "format": "json",
        "list": "categorymembers",
        "cmtitle": "Category:Mobs",
        "cmtype": "page",
        "cmlimit": "max"  # Fetches 500 categories per request
    }
    all_categories = []
    response = session.get(url=URL, params=params)
    data = response.json()
    #pprint(data)

    categories_batch = data.get("query", {}).get("categorymembers", [])
    for cat in categories_batch:
        all_categories.append(cat["title"])
    #pprint(all_categories)
    return all_categories

def web_scrape(topic):

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

        # 2. Output response status immediately to check for server codes (e.g. 403, 503)
        print(f"Server Response Status: {response.status_code}")

        # 3. Attempt safe decoding
        data = response.json()

        # 4. Extract data on successful parsing
        page_html = data["parse"]["text"]["*"]
        soup = BeautifulSoup(page_html, "html.parser")

        print(f"\nSuccess! {topic} Content fetched:")
        text = soup.find_all('p')
        print("\nSuccess! Content cleaned:")
        for p in text:
            clean_text = p.get_text().strip()
            if clean_text != "" and not clean_text.endswith(":"):
                end+=p.text
        #print(end)

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
    topic_dict = {}
    for topic in topics:
        print(f"--------------------------{topic}--------------------------")
        topic_desc = web_scrape(topic)
        topic_dict[topic] = topic_desc
    return topic_dict

def save_json(dictionary, filename):
    with open(filename, "w") as f:
        json.dump(dictionary, f, indent=4)




def pipeline():
    topics = get_categories()
    topic_dict = make_dict(topics)
    save_json(topic_dict, f"topic_dict.json")



pipeline()








