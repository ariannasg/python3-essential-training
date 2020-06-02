#!usr/bin/env python3
# working with JSON data
import json
import urllib.request

# use urllib to retrieve some sample JSON data
req = urllib.request.urlopen("http://httpbin.org/json")
data = req.read().decode('utf-8')
print(data)

# use the JSON module to parse the returned data
obj = json.loads(data)

# when the data is parsed, we can access it like any other object
print(obj["slideshow"]["author"])

for slide in obj["slideshow"]["slides"]:
    print(slide["title"])

# python objects can also be written out as JSON
objdata = {
    "name": "Joe Marini",
    "author": True,
    "titles": [
        "Learning Python", "Advanced Python",
        "Python Standard Library Essential Training"
    ]
}

# writing the above object as json to a file
with open("jsonoutput.json", "w") as fp:
    json.dump(objdata, fp, indent=4)

# CONSOLE OUTPUT:
# {
#   "slideshow": {
#     "author": "Yours Truly",
#     "date": "date of publication",
#     "slides": [
#       {
#         "title": "Wake up to WonderWidgets!",
#         "type": "all"
#       },
#       {
#         "items": [
#           "Why <em>WonderWidgets</em> are great",
#           "Who <em>buys</em> WonderWidgets"
#         ],
#         "title": "Overview",
#         "type": "all"
#       }
#     ],
#     "title": "Sample Slide Show"
#   }
# }
#
# Yours Truly
# Wake up to WonderWidgets!
# Overview
