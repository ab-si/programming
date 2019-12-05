#!/bin/python3

'''
We define super digit of an integer x using the following rules:

    Given an integer, we need to find the super digit of the integer.
    If x has only 1 digit, then its super digit is x.
    Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.

'''

def super_digit(n, k):
    def add_digits(string):
        if len(string) == 1:
            return string
        result = sum(int(s) for s in string)
        return add_digits(str(result))
    
    start = sum(int(s) for s in n) * k
    return add_digits(str(start))

if __name__ == '__main__':
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = super_digit(n, k)
    print(result)
