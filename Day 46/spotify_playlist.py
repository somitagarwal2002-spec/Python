from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"

web = requests.get(URL)
# print(web.status_code)

soup = BeautifulSoup(web.text, "html.parser")
soup.prettify()
class_name = "c-title  a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 u-line-height-normal@mobile-max a-truncate-ellipsis-2line lrv-u-margin-b-025 lrv-u-margin-b-00@mobile-max"

# print(soup.select_one("li.o-chart-results-list__item h3#title-of-a-story"))

song_names = soup.select("li.o-chart-results-list__item h3#title-of-a-story")
song_number = soup.select("li.o-chart-results-list__item span.c-label.a-font-basic")
# print(song_number)

numbers =[]
names = []

# for number in song_number:
#     # print(number.get_text(strip=True))
#     numbers.append(number.get_text(strip=True))

# for song in song_names:
#     # print(song.getText(strip=True))
#     names.append(song.get_text(strip=True))

# for i in range (0,100):
#     print(f"{numbers[i]} {names[i]}")

# Inn teeno loop ki jagah hum ye single loop bhi use kr skte hai 

# for num,son in zip(song_number, song_names):
#     print(f"{num.get_text(strip=True)} {son.get_text(strip=True)}")


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id="0b8b8a74c842461fbc55ed8d3e5873ec",
        client_secret="6550a0e5fa3040cfb2a2a2d34f86a6ac",
        show_dialog=True,
        cache_path="token.txt",
        username="Somit", 
    )
)
user_id = sp.current_user()["id"]




