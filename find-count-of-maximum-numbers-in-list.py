#!/bin/python3

import math
import os
import random
import re
import sys

def Count(ar):
    count=0;
    m=max(ar);
    for i in ar:
        if i==m:
            count=count+1;
    return count;

if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = Count(ar)

    print(result);
    
/*
Input:
4
3 2 1 3

Output:
2
*/
