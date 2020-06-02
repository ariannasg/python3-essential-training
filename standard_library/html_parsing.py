#!usr/bin/env python3
# working with HTML data via the HTMLParser
from abc import ABC, ABCMeta
from html.parser import HTMLParser

metacount = 0


# define a class that will handle various parts of an HTML file
# create a subclass of HTMLParser and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global metacount
        if tag == "meta":
            metacount += 1

        print("Encountered a start tag:", tag)
        pos = self.getpos()  # returns a tuple indication line and character
        print("\tAt line: ", pos[0], " position ", pos[1])

        if len(attrs) > 0:
            print("\tAttributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1])

    # function to handle the ending tag
    def handle_endtag(self, tag):
        print("Encountered an end tag:", tag)

    # function to handle character and text data (tag contents)
    def handle_data(self, data):
        if data.isspace():
            return
        print("Encountered some text data:", data)

    # function to handle the processing of HTML comments
    def handle_comment(self, data):
        print("Encountered comment:", data)


# create an instance of the parser
parser = MyHTMLParser()

# open the sample HTML file and read it
f = open("samplehtml.html")
if f.mode == "r":
    contents = f.read()  # read the entire file
    parser.feed(contents)

print(f"{metacount} meta tags encountered")

# CONSOLE OUTPUT:
# Encountered a start tag: html
# 	At line:  2  position  0
# 	Attributes:
# 	 lang = en
# Encountered a start tag: head
# 	At line:  3  position  0
# Encountered a start tag: meta
# 	At line:  4  position  4
# 	Attributes:
# 	 charset = utf-8
# Encountered an end tag: meta
# Encountered a start tag: title
# 	At line:  5  position  4
# Encountered some text data: Sample HTML Document
# Encountered an end tag: title
# Encountered a start tag: meta
# 	At line:  6  position  4
# 	Attributes:
# 	 name = description
# 	 content = This is a sample HTML file
# Encountered an end tag: meta
# Encountered a start tag: meta
# 	At line:  7  position  4
# 	Attributes:
# 	 name = author
# 	 content = Administrator
# Encountered an end tag: meta
# Encountered a start tag: meta
# 	At line:  8  position  4
# 	Attributes:
# 	 name = viewport
# 	 content = width=device-width; initial-scale=1.0
# Encountered an end tag: meta
# Encountered an end tag: head
# Encountered a start tag: body
# 	At line:  11  position  0
# Encountered comment:  this is a comment
# Encountered a start tag: div
# 	At line:  13  position  0
# Encountered a start tag: header
# 	At line:  14  position  4
# Encountered a start tag: h1
# 	At line:  15  position  8
# Encountered some text data: HTML Sample File
# Encountered an end tag: h1
# Encountered an end tag: header
# Encountered a start tag: nav
# 	At line:  17  position  4
# Encountered a start tag: p
# 	At line:  18  position  8
# Encountered a start tag: a
# 	At line:  19  position  12
# 	Attributes:
# 	 href = /
# Encountered some text data: Home
# Encountered an end tag: a
# Encountered a start tag: a
# 	At line:  20  position  12
# 	Attributes:
# 	 href = /contact
# Encountered some text data: Contact
# Encountered an end tag: a
# Encountered an end tag: p
# Encountered an end tag: nav
# Encountered an end tag: div
# Encountered an end tag: body
# Encountered an end tag: html
# 4 meta tags encountered
