#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    names = [name for name in s.split(" ")]
    for name in range(len(names)):
        if names[name].isalpha():
            names[name] = names[name].title()

    return " ".join(map(str, names))


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    print(solve(s))

    #fptr.write(result + '\n')

    #fptr.close()