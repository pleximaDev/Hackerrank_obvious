#!/bin/python

import math
import os
import random
import re
import sys

def solve(s):
    
    str = s.split(" ")
    print str[0].capitalize()
    for _ in range(0, len(str)):
        str[_] = str[_].capitalize()
    str = " ".join(str)
    return str

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

