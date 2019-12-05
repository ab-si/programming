#!/bin/python3

def weird(n):
    if n%2 != 0:
        print("Weird")
    else:
        if n >= 2 and N<=5:
            print("Not Weird")
        elif n >= 6 and n <= 20:
            print("Weird")
        else:
            print("Not Weird")

def weird2(n):
    if n%2 != 0 and (n > 5 and n < 21):
        print("Weird")
    else:
        print("Not Weird")

if __name__ == '__main__':
    '''
    Given an integer, N , perform the following conditional actions:

    If N is odd, print Weird
    If N is even and in the inclusive range of 2 to 5, print Not Weird
    If N is even and in the inclusive range of  6 to 20, print Weird
    If N is even and greater than 20 , print Not Weird
    '''
    n = int(input())
    weird(n)
