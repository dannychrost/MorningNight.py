import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import datetime
import time
import csv
import datetime
from OpenAITesting import messageCreator
print("Good morning/night script started <3")
while True:
    now = datetime.datetime.now()
    hour = now.hour
    print(now)
    # Spotify API credentials
    USERNAME = ''
    PLAYLIST_ID = ''
    SPOTIPY_CLIENT_ID=''
    SPOTIPY_CLIENT_SECRET=''
    SPOTIPY_REDIRECT_URI=''
    auth_manager = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope= 'playlist-modify-private')
    sp = spotipy.Spotify(auth_manager=auth_manager)

    with open('morning_or_night.csv', mode='r+', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
        if hour >= 6 and hour <= 12:
            if rows[0][0] == '0':
                rows[0][0] = '1'
                rows[1][0] = '0'
                phrase = str(messageCreator("good morning"))
                print(phrase)
                sp.playlist_change_details(playlist_id=PLAYLIST_ID, description=phrase)


        elif hour >= 18 or hour < 6:
            if rows[1][0] == '0':
                rows[1][0] = '1'
                rows[0][0] = '0'
                phrase = str(messageCreator("goodnight"))
                print(phrase)
                sp.playlist_change_details(playlist_id=PLAYLIST_ID, description=phrase)

        file.seek(0) # move the file pointer to the beginning
        writer = csv.writer(file)
        writer.writerows(rows)

    duration = datetime.timedelta(minutes=30)
    time.sleep(duration.total_seconds())  # Sleep for 30 minutes
