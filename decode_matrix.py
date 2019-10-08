#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
decoded = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    column_item = matrix[_]


for _ in range(m):
    for i in range(n):
        decoded.append(matrix[i][_])

print(str(matrix))
print(re.sub('([0-9a-zA-Z]{1})([^0-9a-zA-Z]{1,})([0-9a-zA-Z]{1})', r'\1 \3', "".join(decoded)))

