#!/bin/python

'''
Given a string, s, of length n that is indexed from 0 to n-1 ,
print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line
'''


def review(s):
    a = b = ""
    for i in range(0,len(s)):
        if i==0 or i%2 ==0:
            a += s[i]
        else:
            b += s[i]
    return a, b

def review2(s):
    return s[::2], s[1::2]

n = int(input())
for i in range(n):
    s = input()
    a,b = review2(s)
    print(a, b)
