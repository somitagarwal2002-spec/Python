import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic
import datetime as dt

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
}

URL = "https://appbrewery.github.io/bakeboard-hot-100/2026-04-18/"

response = requests.get(url=URL)
print(response.status_code)
response.raise_for_status()

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
soup.prettify()

class_name = "c-title  a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 u-line-height-normal@mobile-max a-truncate-ellipsis-2line lrv-u-margin-b-025 lrv-u-margin-b-00@mobile-max"

song_names = soup.select("div.chart-entry__info h3.chart-entry__title") 
# html tag ke baad agar hum class likh rhe hai to hum keval tagname.classname aise likh skte hai but agr hum
# id likh rhe hai tag ke sath to tagname#id aise likhna hoga

song_number = soup.select("div.chart-entry__rank span.chart-entry__rank-number")

# print(song_number)

song_names_list = []
song_number_list = []

for song, number in zip(song_names, song_number) :
# jb hum do variables aur do list pr ek sath kaam krna chah rhe ho to hum zip ka use krte hai
    song_names_list.append(song.get_text(strip=True))
    song_number_list.append(number.get_text(strip=True))

# print(song_names_list)
# print(song_number_list)

yt = YTMusic("Day 46/browser.json")
playlists = yt.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")

date = dt.datetime.now().strftime("%H:%M:%S")

playlist_id = yt.create_playlist(
    title=f"{date} Billboard 100 Playlist",
    description="Somit's Wonderful Playlist"
)

# print(playlist_id)

# print(playlists[:2])

results = yt.search("Blinding Lights", filter="songs")

# print(results[0])

video_id = results[0]["videoId"]

yt.add_playlist_items(
    playlist_id,
    [video_id]
)

print(playlist_id)
print(results[0])
print(playlists[:1])

for song in song_names_list:
    try:
        results = yt.search(song, filter="songs")

        if not results:
            continue

        first_result = results[0]

        if "videoId" not in first_result:
            print(f"No videoId found for {song}")
            continue

        video_id = first_result["videoId"]

        yt.add_playlist_items(
            playlist_id,
            [video_id]
        )

        print(f"Added: {song}")

    except Exception as e:
        print(f"Failed: {song}")
        print(e)

print("Playlist Created Successfully")







