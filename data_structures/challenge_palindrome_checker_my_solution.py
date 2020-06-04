#!usr/bin/env python3
from data_structures.custom_deque import Deque


# Use a deque data structure and write a function that takes in an input
# string.
# The function should return true if the string is a palindrome or false if
# the string is not a palindrome.
# As a reminder, a palindrome is a word that is spelled the same backwards
# and forwards. Some examples would be mom, level, and kayak.


def is_palindrome(word):
    if not isinstance(word, str):
        raise TypeError('word must be a string')

    if len(word) == 0:
        raise ValueError('word must have at least one character')

    reversed_word_deque = Deque()
    for character in word:
        reversed_word_deque.add_front(character)

    if ''.join(reversed_word_deque.items) == word:
        return True
    else:
        return False


assert is_palindrome('mom') is True
assert is_palindrome('level') is True
assert is_palindrome('kayak') is True
assert is_palindrome('school') is False
assert is_palindrome('night') is False
assert is_palindrome('book') is False
