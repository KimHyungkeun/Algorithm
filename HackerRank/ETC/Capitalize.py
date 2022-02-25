#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    ans = []
    s = list(s)
    for i in range(len(s)) :
        if i == 0 and ('a' <= s[0] <= 'z' or 'A' <= s[0] <= 'Z') :
            s[0] = s[0].upper()
        elif ('a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z') and s[i-1] == ' ' :
            s[i] = s[i].upper()
    
    return ''.join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
