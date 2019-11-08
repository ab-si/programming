'''
Two strings are anagrams of each other if the letters of one string can be
rearranged to form the other string.
Given a string, find the number of pairs of substrings of the string that are
anagrams of each other.
'''

import os
from collections import Counter

def anagram(s):
    count = 0
    for i in range(1, len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        b = Counter(a)
        for j in b:
            count += b[j]*(b[j]-1)/2
    return count

if __name__ == "__main__":
    s = "qwertytrewewrtwerer"
    res = anagram(s)
    print(res)