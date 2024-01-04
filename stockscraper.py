import re
import urllib.request

## our url https://www.google.com/finance/quote/TSLA:NASDAQ

url = "https://www.google.com/finance/quote/"
stock = input("Enter stock ticker in all caps: ")
url1 = url + stock + ":NASDAQ"
data = urllib.request.urlopen(url1).read()
data1 = data.decode("utf-8")
search = re.search('data-last-price="', data1)
print(search)

start = search.start()
end = start + 25
print(data1[start:end])
price = data1[start:end]
print(price)
real_price = price[17:]
print(real_price)
rrprice = re.search('"',real_price)
rstart = 0
rrend = rrprice.end() - 1
test_price = real_price[rstart:rrend]
final_price = "Your stock choice, " + stock.upper() + ", has a price of " + test_price + "."
print(final_price)
