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
    ltr = 0
    rtl = 0
    for i in range(len(arr)):
        ltr += int(arr[i][i])
        rtl += int(arr[i][len(arr) - i - 1])

    if ltr > rtl:
        return ltr - rtl
    else:
        return rtl - ltr


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(str(result) + '\n')

    #fptr.close()
