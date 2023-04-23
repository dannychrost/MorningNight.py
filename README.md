# MorningNight.py

A Python script to dynamically update a Spotify playlist description.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To use this script, you should have the following installed on your local machine:

- Python
- Spotipy library
  -OpenAI library

### Installing

1. Clone the repository to your local machine.
2. Install the Python interpreter and the Spotipy as well as OpenAI libraries.

### Usage

1. Create two csv files with the names morning_or_night.csv (UTF-8 comma delimited) and phrases.csv (command delimited). Fill the first column of the first row in phrases.csv out with something random otherwise the program won't work. Fill the first column of the first and second rows in morning_or_night.csv out with the number 0 in each (these value will change when you start to finally run the program)
2. Using the Spotify Developer Dashboard, click "Create App". For the redirect URI, you can use something like http://localhost:8089/callback
3. In the MorningNight.py script, fill out the information for the following variables: "USERNAME" (can be found on your Spotify Account Overview page); "PLAYLIST_ID" (in the playlist's link, it is between 'playlist/' and '?'); "SPOTIPY_CLIENT_ID"; "SPOTIPY_CLIENT_SECRET"; and the "SPOTIPY_REDIRECT_URI" that you previously created
4. In the OpenAITesting.py script, you need to put your API key into the quotes of the variable "openai.api_key". It can be created on the following website: https://platform.openai.com/
5. Run the script from the project folder on VSCode or your own terminal using this command "py MorningNight.py"

### Known Issues

phrases.csv requires a header row so that is why you must fill out the first column of the first row initially

### Sidenotes

If you want to generate a new message without waiting, close the execution of the program (if any) and just reset the values in morning_or_night.csv to 0.

If you want to change the prompt in OpenAITesting.py, change it from within the "prompt" variable, remove "{time}", remove "time" from "def messageCreator(time):". Inside MorningNight.py, remove "good morning" and "goodnight" with quotes from "phrase = str(messageCreator("good morning"))" and "phrase = str(messageCreator("goodnight"))"
