################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import urllib.request # module defines functions and classes which help in opening URLs
import time
import json # JavaScript Object Notation - lightweight data-interchange format that is used to store and exchange data. 
import random # module produces pseudo-random numbers

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# Number of server requests
N = 500

def getDataPoint(quote):
	# getDataPoint function should return correct tuple of stock name, bid_price,
	# ask_price and price. Note: price of a stock = average of bid and ask
	# Example of a quote:
	# [{"id": "0.1", "stock": "ABC", "timestamp": "2020-07-09 05:23:25.038269", "top_bid": {"price": 126.12, "size": 279}, "top_ask": {"price": 125.05, "size": 12}}, 
	# {"id": "0.1", "stock": "DEF", "timestamp": "2020-07-09 05:23:25.038269", "top_bid": {"price": 124.66, "size": 7}, "top_ask": {"price": 125.05, "size": 53}}]
	stock = quote['stock']
	bid_price = float(quote['top_bid']['price'])
	ask_price = float(quote['top_ask']['price'])
	price = float('{:.2f}'.format((bid_price + ask_price)/2))
	return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
	# getRatio function should return the ratio of the two stock prices

	if (price_b == 0):
		return
	return price_a/price_b

# Main
# Main function should output correct stock info, prices and ratio
if __name__ == "__main__":

	# Query the price once every N seconds.
	for _ in iter(range(N)):
		# random.random() : Return the next random floating point number in the range [0.0, 1.0).
		# urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None) - 
		# - Open the URL url, which can be either a string or a Request object.
		# json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary. 
		# It is mainly used for deserializing native string, byte, or byte array which consists of JSON data into Python Dictionary.
		quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read()) # quotes <class 'list'>
		prices = {} # create an empy dict to capture prices for getRation 
		for quote in quotes: # Two quotes: 'ABC', 'DEF'
			stock, bid_price, ask_price, price = getDataPoint(quote)
			prices[stock] = price
			print ("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

		print ("Ratio %s" % getRatio(prices['ABC'], prices['DEF']))
