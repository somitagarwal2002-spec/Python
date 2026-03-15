from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

movie = list(soup.select("div.entity-info-items__list a"))
# print(type(movie))
# print(movie)

names = []

for m in range(0, len(movie)):
    # print(movie[m])
    names.append(movie[m].getText())

# upar wale loop ki jagah isko bhi use kr skte the
# best yhi tareeka hai

# for m in movie:
#     names.append(m.get_text(strip=True))


# Reversing List
# Method 1
names = names[::-1]

# Method 2
# for n in range(len(names) - 1, -1, -1):
        # print(names[n])

for name in range(0, len(names)):
    print(f"{name + 1}: {names[name]}")
