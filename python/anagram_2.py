#!/bin/python3
'''
We consider two strings to be anagrams of each other if
the first string's letters can be rearranged to form the second string.
In other words, both strings must contain the same exact letters in the same exact frequency.

Given two strings, a and b, that may or may not be of the same length,
determine the minimum number of character deletions required to make a and b anagrams.
Any characters can be deleted from either of the strings.
'''

from collections import Counter

def make_anagram(a, b):
    count_a = Counter(a)
    count_b = Counter(b)
    val1 = count_a-count_b
    val2 = count_b-count_a
    return (sum(val1.values()) + sum(val2.values()))

if __name__ == '__main__':
    a = input()
    b = input()
    res = make_anagram(a, b)
    print(res)
