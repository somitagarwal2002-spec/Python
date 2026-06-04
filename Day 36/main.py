import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "my_stock_api_key"
NEWS_API_KEY = "my_news_api_key"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
print(response.status_code)
response.raise_for_status()

data = response.json()
# print(data)

data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
# print(data_list)
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday = data_list[4]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]
print(day_before_yesterday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

differemce = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price)) 
# abs lagane se hume negative mein value nhi milegi
print(round(differemce, 2))

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage_change = ( differemce / float(yesterday_closing_price) ) * 100
print(round(percentage_change, 2))

#TODO 5. - If TODO4 percentage is greater than 4 then print("Get News").

if percentage_change > 4:
    print("Get News")

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

if percentage_change > 4:
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    # print(news_response.status_code)
    news_response.raise_for_status()
    # print(news_response.json())
    articles = news_response.json()["articles"]
    # print(articles)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    first_three_articles = articles[:3]
    # print(first_three_articles)
    # print(first_three_articles[0]["title"])
