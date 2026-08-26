
from pprint import pprint

import requests
from bs4 import BeautifulSoup

URL = "https://minecraft.wiki/api.php"

#WORKING ON SCRAPING MULTIPLE TOPICS
topics = ["Diamond Ore", "Creeper"]

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

        print("\nSuccess! Content fetched:")

        text = soup.find_all('p')
        print("\nSuccess! Content cleaned:")
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


def make_dict(topic):
    topic_dict = {}
    for topic in topics:
        topic_desc = web_scrape(topic)
        topic_dict[topic] = topic_desc
    pprint(topic_dict)

make_dict(topics)
