#!/bin/python3

import os

#
# Complete the 'solution' function below.
#
# The function is expected to return a FLOAT.
# The function accepts following parameters:
#  1. STRING_ARRAY bag_arr
#  2. STRING_ARRAY draw_arr
#

def fact(n):
    if n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1,n + 1):
            factorial = factorial*i
        return factorial


def npr(n, r):
    return fact(n) / fact(n-r)


def solution(bag_arr, draw_arr):
    # Write your code here
    num = len(bag_arr)
    br = {x: bag_arr.count(x) for x in bag_arr}
    dr = {x: draw_arr.count(x) for x in draw_arr}

    BR = list(set(bag_arr))
    DR = list(set(draw_arr))

    NPR = []
    for i in DR:
        if i in dr.keys():
            if i in br:
                n = br[i]
                r = dr[i]
                NPR.append(npr(n, r))
            else:
                return 0

    prod = 1
    for i in NPR:
        prod = prod * i

    final = prod / npr(num, len(draw_arr))

    return final


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bag_arr_count = int(input().strip())

    bag_arr = []

    for _ in range(bag_arr_count):
        bag_arr_item = input()
        bag_arr.append(bag_arr_item)

    draw_arr_count = int(input().strip())

    draw_arr = []

    for _ in range(draw_arr_count):
        draw_arr_item = input()
        draw_arr.append(draw_arr_item)

    result = solution(bag_arr, draw_arr)

    fptr.write(str(float(result)) + '\n')

    fptr.close()


