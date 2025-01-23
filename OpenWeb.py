import requests

YahooFinanceAddress = "https://finance.yahoo.com/quote/"

def YahooFinanceURL(ticker):
    return YahooFinanceAddress + ticker

def YahooFinanceURLs(tickers):
    return [YahooFinanceURL(ticker) for ticker in tickers]

#Open website and then pull in the html
r = requests.get(YahooFinanceURL("AAPL"))
print(r.text)


#Sample Ollama curl command
# curl http://localhost:11434/api/generate -d '{
#   "model": "llama3.2",
#   "prompt":"Why is the sky blue?"
# }'

# Break 