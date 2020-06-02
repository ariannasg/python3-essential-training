#!usr/bin/env python3
# retrieve data from the internet
import urllib.request

sample_url = "http://httpbin.org/xml"

# Create a request to retrieve data using urllib.request
resp = urllib.request.urlopen(sample_url, timeout=5)

# Check the status
status_code = resp.status
print(status_code)

# if no error, then read the response contents
if 200 <= status_code < 300:
    # work with response headers
    print(resp.getheaders())
    print(resp.getheader('Content-length'))
    print(resp.headers['Content-Type'])

    # read the data from the URL
    # use the decode for converting the bytes into text
    data = resp.read().decode('utf-8')
    print(data)

# CONSOLE OUTPUT:
# 200
# [('Date', 'Tue, 02 Jun 2020 08:33:35 GMT'), ('Content-Type', 'application/xml'), ('Content-Length', '522'), ('Connection', 'close'), ('Server', 'gunicorn/19.9.0'), ('Access-Control-Allow-Origin', '*'), ('Access-Control-Allow-Credentials', 'true')]
# 522
# application/xml
# <?xml version='1.0' encoding='us-ascii'?>
#
# <!--  A SAMPLE set of slides  -->
#
# <slideshow
#     title="Sample Slide Show"
#     date="Date of publication"
#     author="Yours Truly"
#     >
#
#     <!-- TITLE SLIDE -->
#     <slide type="all">
#       <title>Wake up to WonderWidgets!</title>
#     </slide>
#
#     <!-- OVERVIEW -->
#     <slide type="all">
#         <title>Overview</title>
#         <item>Why <em>WonderWidgets</em> are great</item>
#         <item/>
#         <item>Who <em>buys</em> WonderWidgets</item>
#     </slide>
#
# </slideshow>
