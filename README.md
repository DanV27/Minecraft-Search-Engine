# Minecraft Search Engine

A search engine for the Minecraft Wiki: a scraper builds a searchable index of
wiki topics, a Flask API serves search results, and a React frontend lets you
search them from the browser.

## How it works

- **`scraper.py`** — Crawls the Minecraft Wiki, collects topics and their
  descriptions, and saves them to `data/topic_dict.json`.
- **`reverse.py`** — Turns that scraped data into a word-to-topic index
  (`data/index.json`), where each key is a word and its value is a dict of
  topics containing that word, mapped to how many times it appears. Example:
  ```
  "explosion": {"creeper": 5, "tnt": 4, "end crystal": 3, "trap door": 1}
  ```
- **`search.py`** — Looks up a search term in the index and returns matching
  topics ordered by relevance.
- **`app.py`** — A Flask API (`POST /`) that wraps `search.py` so the frontend
  can query it over HTTP.
- **`minesearchReact/`** — The React frontend (built with Vite) that calls the
  Flask API and displays results.

## Project structure

```
.
├── app.py                # Flask API
├── search.py              # Search logic
├── scraper.py              # Wiki scraper
├── reverse.py               # Builds the search index from scraped data
├── data/                      # Generated JSON data (index + topic descriptions)
├── minesearchReact/             # React frontend (Vite)
└── requirements.txt               # Python dependencies
```

## Setup

### Backend (Flask API)

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

The API runs on `http://127.0.0.1:5000`.

### Frontend (React)

```
cd minesearchReact
npm install
npm run dev
```

Opens at `http://localhost:3000`. Make sure the Flask API is running first —
the frontend calls it directly.

### Rebuilding the search data

If you want to re-scrape the wiki and rebuild the index yourself:

```
python scraper.py
python reverse.py
```

## Roadmap

- Some topics (biomes being the big one) still aren't fully parsed into the
  scraped data.
- Multi-word search — right now search is single-term; a union search across
  multiple words would be a nice addition.
- Continue polishing the React UI.
