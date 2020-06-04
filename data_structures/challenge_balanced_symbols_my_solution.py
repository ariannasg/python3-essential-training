#!usr/bin/env python3
from data_structures.stack import Stack

# In this challenge, your prompt is to create a function that takes in a
# string of symbol pairs as a parameter.
# The function should return true if the symbol string is balanced or
# false if it isn't.
# In order for symbols to be balanced, each opening symbol should also have
# a closing symbol. And the symbols must be properly nested.
# You should make use of a stack in your solution.
# Example of balanced symbols: ([{}]) ([]{}()) ((()))
# Example of unbalanced symbols: (([{]) [}([){]

allowed_symbols = {'(': ')',
                   '[': ']',
                   '{': '}'}


def is_balanced(symbols):
    if not isinstance(symbols, str):
        raise TypeError('symbols must be a string')

    if len(symbols) == 0:
        raise ValueError('symbols must have at least one symbol')

    stack = Stack()
    for symbol in symbols:
        if stack.is_empty():
            stack.push(symbol)
        else:
            top_symbol = stack.peek()
            if allowed_symbols.get(top_symbol, None) == symbol:
                stack.pop()
            else:
                stack.push(symbol)

    if stack.is_empty():
        return True

    return False


assert is_balanced('([{}])') is True
assert is_balanced('([]{}())') is True
assert is_balanced('((()))') is True
assert is_balanced('(([{])') is False
assert is_balanced('[}([){]') is False
assert is_balanced('[') is False
