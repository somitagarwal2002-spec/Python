from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# print(soup.title) jo tab mein likha hoga wo aa jayega

articles = soup.find_all("a", class_="storylink")
articles_text = []
articles_links = []

for article_tag in articles:
    text = article_tag.getText()
    articles_text.append(text)
    link = article_tag.get("href")
    articles_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]


print(articles_text)
print(articles_links)
print(article_upvote)

largest_number = max(article_upvote)
# print(largest_number)

largest_number_index = article_upvote.index(largest_number)
# print(largest_number_index)

print(articles_text[largest_number_index])
print(articles_links[largest_number_index])
print(article_upvote[largest_number_index])
