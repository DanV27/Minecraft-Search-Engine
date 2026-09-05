# Minecraft Search Engine

### What it can do so far: 
#### Scraper.py:   
Goes through minecraft wiki and scrapes all the topcis it can find currently and gets their description, saves this into a JSON file.  
#### Reverse.py.  
Takes the json from scaper and turns into a dictionary that the search engine can use. so key values are all the possible words,   
and their value is a dictionary of topics that word is in and number, this number is how many times that topic has that specific word!   
for example:   
"explosion": {"creeper": 5 , "tnt": 4 , "end crystal": 3, "Trap door": 1}   
#### Search.py.  
This file is a basic search engine CLI.   
Ask the user for something it's looking for and thrn gives back a list of topics.   
Of course the topics are in order for most relevant




### What it I plan for it to do:   
 Right now there are certain topics that did get parsed into JSON (a big one being biomes).   
Also I'd like for the ability for a user to search with multiple words, and the search engine being able to take the union search of both of them.   
 A UI screen would be nice touch as well.