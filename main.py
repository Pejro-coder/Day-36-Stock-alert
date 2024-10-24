import time
import requests
import datetime as dt
import json

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = "UBVHBKXM4YSYW6BX"

# ---------------------------- Daily API request ---------------------------
# parameters_daily = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK,
#     "apikey": STOCK_API,
# }
# response_daily = requests.get(url="https://www.alphavantage.co/query", params=parameters_daily)
# response_daily.raise_for_status()
# data_daily = response_daily.json()

with open("yesterday_daily.json", "r") as file:
    data_daily = json.load(file)
    print(data_daily)


# ---------------------- Hourly
# parameters_hourly = {
#     "function": "TIME_SERIES_INTRADAY",
#     "interval": "60min",
#     "symbol": STOCK,
#     "apikey": STOCK_API,
# }
# response_hourly = requests.get(url="https://www.alphavantage.co/query", params=parameters_hourly)
# response_hourly.raise_for_status()
# data_hourly = response_hourly.json()


# Get yesterday's date, from today's date, so it can be used to filter out yesterday's closing price in the json
print()
today_date = dt.datetime.now().date()
year = today_date.year
month = today_date.month
day = today_date.day
yesterday = day - 1
yesterday_date = f"{year}-{month}-{yesterday}" #YESTERDAY's DATE
today_date = f"{dt.datetime.now().date()}"

print(f"today:    {today_date}")
print(type(today_date))
print(f"yesterday {yesterday_date}")
print(type(yesterday_date))

yesterday_closing_price = data_daily["Time Series (Daily)"][yesterday_date]["4. close"]
print(yesterday_closing_price)
today_opening_price = data_daily["Time Series (Daily)"][today_date]["4. close"]

# print(today_opening_price / yesterday_closing_price)

yesterday_closing_price = data_daily["Time Series (Daily)"]




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
























