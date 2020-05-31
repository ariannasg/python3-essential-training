#!usr/bin/env python3
from string import Template


# there are at least 4 ways of formatting a string in python.
# the format method can be very powerful since it allows us to specifier for
# spacing, number formatting, justification and so on; but might some
# vulnerability issues for being so powerful.

# template strings is one way to format them. why use this way? 2 reasons:
# 1. if all you need to do is simple variable substitution then the template
# string method is more simple to use and makes the code more readable.
# 2. in case the template is being supplied from a source you don't really
# know or you don't really trust -> is more secure to use the template method
# than the format function. if we need to add extra security when formatting
# strings, then we need to use the template method
def main():
    # Usual/Regular string formatting with format()
    str1 = "You're watching {0} by {1}".format('Advanced Python', 'Joe Marini')
    print(str1)

    # create a template with placeholders
    templ = Template("You're watching ${title} by ${author}")

    # use the substitute method with keyword arguments
    str2 = templ.substitute(title="Advanced Python", author="Joe Marini")
    print(str2)

    data = {
        "title": "Advanced Python",
        "author": "Joe Marini",
    }

    # use the substitute method with a dictionary
    str3 = templ.substitute(data)
    print(str3)


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# You're watching Advanced Python by Joe Marini
# You're watching Advanced Python by Joe Marini
# You're watching Advanced Python by Joe Marini
