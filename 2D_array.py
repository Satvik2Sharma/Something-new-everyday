# Given a 6x6 2D array, arr, an hourglass is a subset of values with indices falling in the following pattern:
#  a b c  
#    d  
#  e f g
# HackerRank



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
def hourglassSum(arr):
    max_sum = -9 * 7
    for i in range(4):
        for j in range(4):
            current_sum = (
                arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            )
            max_sum = max(max_sum, current_sum)
    return max_sum
    
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
