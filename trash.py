import requests

URL = "https://minecraft.wiki/api.php"  # Replace with your specific wiki API endpoint

PARAMS = {
    "action": "query",
    "list": "allcategories",
    "aclimit": "max",  # Fetch the maximum allowed per request (500 for users)
    "format": "json"
}

categories = []

while True:
    response = requests.get(url=URL, params=PARAMS).json()

    # Extract categories from the current page
    if "query" in response and "allcategories" in response["query"]:
        for cat in response["query"]["allcategories"]:
            categories.append(cat["*"])  # The category name is stored under the '*' key

    # Check for a continuation token to handle pagination
    if "continue" in response:
        PARAMS.update(response["continue"])
    else:
        break

print(f"Fetched {len(categories)} distinct categories.")
print(categories)  # View the first 10 items
