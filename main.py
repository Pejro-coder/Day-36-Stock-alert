import time
import requests
import datetime as dt
import json
from twilio.rest import Client



# ------------------------------- News data ------------------------------
news_params = {
    "q": COMPANY_NAME,  # Search for articles about Tesla
    "apiKey": NEWS_API_KEY,
    "pageSize": 10,  # Limit to top 3 articles
    "language": "en",  # Articles in English
    "sortBy": "publishedAt"  # Sort by the most recent articles
}

news_response = requests.get("https://newsapi.org/v2/top-headlines", params=news_params)
news_response.raise_for_status()  # Check for errors in the request

news_data = news_response.json()
print(news_data)
news_to_send = (news_data["articles"][0]["description"])

# ------------------------- Daily stock data API request ------------------------
# parameters_daily = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK,
#     "apikey": STOCK_API,
# }
# response_daily = requests.get(url="https://www.alphavantage.co/query", params=parameters_daily)
# response_daily.raise_for_status()
# data_daily = response_daily.json()


# testing file, cause API requests are limited to 25 on free
with open("today_daily_update.json", "r") as file:
    data_daily = json.load(file)
    print(data_daily)

# ---------------------------- Get yesterday's date, from today's date,
# so it can be used to filter out yesterday's closing price in the json ----------------------------
print()
today_date = dt.datetime.now().date()
year = today_date.year
month = today_date.month
day = today_date.day
yesterday = day - 1
yesterday_date = f"{year}-{month}-{yesterday}"  #YESTERDAY's DATE

# ---------------------------- Yesterday's closing price & Today's opening price ----------------------------
today_date = f"{dt.datetime.now().date()}"

yesterday_closing_price = float(data_daily["Time Series (Daily)"][yesterday_date]["4. close"])
today_opening_price = float(data_daily["Time Series (Daily)"][today_date]["4. close"])
print(f"today:    {today_date}, opening price: {today_opening_price}")
print(f"yesterday {yesterday_date}, closing price: {yesterday_closing_price}")
price_ratio = today_opening_price / yesterday_closing_price
print(f"Price ratio: {price_ratio}")
percentage_change = round((price_ratio - 1) * 100, )
print(percentage_change)


# ---------------------------- Send SMS ----------------------------
def twilio_send():
    print(text)
    account_sid = TWILIO_account_sid
    auth_token = TWILIO_auth_token
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=text,
        from_="+12028048453",
        to="+38640555904",
    )

    print(message.body)


if price_ratio > 1.05:
    text = f"{COMPANY_NAME}🚀 +{percentage_change}% \n{news_to_send}"
    twilio_send()
elif price_ratio < 0.95:
    text = f"{COMPANY_NAME}🔻{percentage_change}% \n{news_to_send}"
    twilio_send()



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' 
portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' 
and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
