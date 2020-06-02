#!usr/bin/env python3
# Using the URL parsing functions to deconstruct and parse URLs
import urllib.parse

sample_url = "https://example.com:8080/test.html?val1=1&val2=Hello+World"

# parse a URL with urlparse()
result = urllib.parse.urlparse(sample_url)
print(result)
print('scheme:', result.scheme)
print('hostname:', result.hostname)
print('path:', result.path)
print('port:', result.port)
print('url:', result.geturl())


# in order to use special chars (space,ñ) un a url we need to convert them
# quote() replaces special characters for use in URLs
sample_string = "Hello El Niño"
print(urllib.parse.quote(sample_string))
print(urllib.parse.quote_plus(sample_string))


# how to convert dict of values into parameter strings for using in a URL as
# part of the query string
# Use urlencode() to convert maps to parameter strings
query_data = {
    'Name': "John Doe",
    "City": "Anytown USA",
    "Age": 37
}
result = urllib.parse.urlencode(query_data)
print(result)


# CONSOLE OUTPUT:
# ParseResult(scheme='https', netloc='example.com:8080', path='/test.html', params='', query='val1=1&val2=Hello+World', fragment='')
# scheme: https
# hostname: example.com
# path: /test.html
# port: 8080
# url: https://example.com:8080/test.html?val1=1&val2=Hello+World
# Hello%20El%20Ni%C3%B1o
# Hello+El+Ni%C3%B1o
# Name=John+Doe&City=Anytown+USA&Age=37
