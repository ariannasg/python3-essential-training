#!usr/bin/env python3


# python provides a way for specifying function parameters using keywords.
# we can define a function that takes positional arguments along with keyword
# arguments that take optional values. Then, when you want to call the
# function, you can specify values by position or by keyword.
# sometimes we want to enforce calling a function by specifying parameters by
# keyword, since it can improve the readability of the code and can make it
# safer in case the parameter has a significant effect on how the program runs.
# This way, the function caller is aware of the significance of the parameter
# and others who read the code can easily see and understand what's happening.
# To accomplish this we can separate the positional arguments with a single
# asterisk character followed by parameters that are keyword-only.
# if we really need to make sure that someone using a particular function
# clearly understands what they're doing and why they're doing it, we can use
# keyword-only arguments to help ensure clarity in the code.

# use keyword-only arguments to help ensure code clarity
def my_function(arg1, arg2, *, suppress_exceptions=False):
    print(arg1, arg2, suppress_exceptions)


def my_function2(*, arg1, arg2):
    print(arg1, arg2)


def main():
    # if we try to call the function without the keyword we'll get
    # "TypeError: my_function() takes 2 positional arguments but 3 were given"
    # my_function(1, 2, True)
    my_function(1, 2, suppress_exceptions=True)
    my_function(arg2=1, arg1=2, suppress_exceptions=True)

    # my_function2(1,2)   # will throw
    # TypeError: my_function2() takes 0 positional arguments but 2 were given
    my_function2(arg1=1, arg2=2)


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# 1 2 True
# 2 1 True
# 1 2
