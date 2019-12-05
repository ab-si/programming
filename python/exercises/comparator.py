#!/bin/python3
'''
Given an array of n Player objects, write a comparator that sorts them in order of decreasing score.
If 2 or more players have the same score, sort those players alphabetically ascending by name.
To do this, you must create a Checker class that implements the Comparator interface,
then write an int compare(Player a, Player b) method implementing the
Comparator.compare(T o1, T o2) method. In short, when sorting in ascending order,
a comparator function returns -1 if a<b, 0 if a=b, and 1 if a>b.
'''

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        pass
    def comparator(a, b):
        val = b.score - a.score
        if val == 0:
            return -1 if a.name < b.name else 1
        return val

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)