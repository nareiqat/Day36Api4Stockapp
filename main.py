import requests
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "123123"
NEWS_API_KEY = "129378as7d897da"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
r = requests.get(STOCK_ENDPOINT, params=parameters)
data = r.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_closing_stock = data_list[0]["4. close"]

print(yesterday_closing_stock)

day_before_yesterday_closing_stock = data_list[1]["4. close"]

positive_difference = round(abs(yesterday_closing_stock) - float(day_before_yesterday_closing_stock), 3)
print(positive_difference)


percentage_difference = round(positive_difference / float(day_before_yesterday_closing_stock), 2) * 100
print(percentage_difference)


news_parameters = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME
}


news_request = requests.get(NEWS_ENDPOINT, params=news_parameters)
news_request.raise_for_status()
news_articles = news_request.json()["articles"]

news_list = news_articles[:3]

print(news_list)

news_info = []
for article in news_list:
    news_info.append(f"Headline:{article['title']} ,\nBrief: {article['description']}")
print(news_info)

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user="user@gmail.com", password="somepassword")
    connection.sendmail(from_addr="someemail@gmail.com", to_addrs="some1email@gmail.com", msg=news_info[0])


