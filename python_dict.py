#!/bin/python3

'''
Given n names and phone numbers, assemble a phone book that maps friends' names
to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for.
For each 'name' queried, print the associated entry from your phone book on a new line
name=phoneNumber;
if an entry for  is not found, print Not found instead.
'''

def add_to_dict(x, d):
    d[x[0]] = x[1]
    return d

def search_and_print(query, d):
    if query in d:
        print("{}={}".format(query, d[query]))
    else:
        print("Not found")

if __name__ == '__main__':
    d = {}
    n = int(input())
    for i in range(0, n):
        x = input().split()
        d = add_to_dict(x, d)
    while True:
        try:
            search_and_print(input(), d)
        except EOFError:
            break
        
