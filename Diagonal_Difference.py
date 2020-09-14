#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    s1 = 0
    s2 = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            s1 += arr[i][j]
            s2 += arr[i][len(arr) - 1 - i]

    return abs(s1 - s2)


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)


