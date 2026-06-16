#!/bin/python3

import math
import os
import random
import re
import sys
import sys
sys.set_int_max_str_digits(0)
#sys.set_int_max_str_digits(10**6)
#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#

def fibonacciModified(t1, t2, n):
    # Write your code here

    # if n == 1:
    #     return t1
    # if n == 2:
    #     return t2
    # for _ in range(3, n + 1):
    #     t1, t2 = t2, t1 + t2 * t2
    # return t2


    # if n <= 1:
    #     return t1
    # if n == 2:
    #     return t2
    # seq = [0] * (n + 1)
    # seq[1] = t1
    # seq[2] = t2
    # for i in range(3, n + 1):
    #     seq[i] = seq[i - 2] + seq[i - 1] * seq[i - 1]
    # return seq[n]


    # if n <= 0:
    #     return 0
    # if n == 1:
    #     return t1
    # if n == 2:
    #     return t2
    # fib = [0] * (n + 1)
    # fib[1] = t1
    # fib[2] = t2
    # for i in range(3, n + 1):
    #     fib[i] = fib[i - 2] + fib[i - 1] * fib[i - 1]
    # return fib[n]
    
    
    
    # for _ in range(n - 2):
    #     t1, t2 = t2, t1 + (t2 ** 2)
    # return t2
    
    

    # for _ in range(3, n + 1):
    #     t1, t2 = t2, t1 + t2 * t2
    # return t2




    for _ in range(3, n + 1):
        t1, t2 = t2, t1 + t2 * t2
    return t1 if n == 1 else t2



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
