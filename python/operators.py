#!/bin/python3

import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)
    return int(round(meal_cost + tip + tax))

if __name__ == '__main__':
    '''
    This program returns the total cost for the meal rounded to
    the nearest integer
    '''
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    total = solve(meal_cost, tip_percent, tax_percent)
    print(total)
