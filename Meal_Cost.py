import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    Tip = (meal_cost * tip_percent)/100
    Tax = (meal_cost * tax_percent)/100
    Total = int(round(meal_cost + Tip + Tax))
    return Total


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print(solve(meal_cost, tip_percent, tax_percent))