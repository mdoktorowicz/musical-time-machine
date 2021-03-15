from bs4 import BeautifulSoup
import requests
import spotipy
import os

URL_init = "https://www.billboard.com/charts/hot-100/"
client_id = os.environ.get("spotify_client_id")
client_secret = os.environ.get("spotify_client_secret")
redirect_url = os.environ.get("redirect_url")
song_list = []

date = input("What date do you want to get music from? Input format: YYYY-MM-DD ")
URL_final = URL_init + date
year = date[:4]

response = requests.get(URL_final)
website_data = response.text

soup = BeautifulSoup(website_data, "html.parser")

full_class = soup.find_all(class_="chart-element__information__song text--truncate color--primary")

for song in full_class:
    title_text = song.getText()
    clean_title = title_text.replace(" ", "%20")
    song_list.append(clean_title)

auth = spotipy.oauth2.SpotifyOAuth(client_id=client_id,
                                      client_secret=redirect_url,
                                      redirect_uri="http://example.com",
                                      state=None,
                                      scope="playlist-modify-private",
                                      cache_path="token.txt",
                                      username=None,
                                      proxies=None,
                                      show_dialog=True,
                                      requests_session=True,
                                      requests_timeout=None)

spotify = spotipy.client.Spotify(auth=auth.get_access_token(as_dict=False),
                                 requests_session=True,
                                 client_credentials_manager=None,
                                 oauth_manager=auth,
                                 auth_manager=auth,
                                 proxies=None,
                                 requests_timeout=5,
                                 status_forcelist=None,
                                 retries=3,
                                 status_retries=3,
                                 backoff_factor=0.3)

username = spotify.current_user()["id"]

playlist_name = input("What's the new playlist name? ")
new_playlist_info = spotify.user_playlist_create(username, playlist_name, public=False, collaborative=False, description='test')

n = 0
results_list = []
for n in range(len(song_list)):
    results = spotify.search(q=f"track: {song_list[n]} year: {year}", type="track")

    try:
        track = results["tracks"]["items"][0]["external_urls"]["spotify"]
        results_list.append(track)

    except IndexError:
        pass

    finally:
        n += 1

spotify.playlist_add_items(playlist_id=new_playlist_info["id"], items=results_list)