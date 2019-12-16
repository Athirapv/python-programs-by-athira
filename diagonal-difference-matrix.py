#!/bin/python3

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    dial=0;
    diar=0;
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            if i==j:
                dial=dial+arr[i][j];
            if ((i+j)==(len(arr)-1)):
                diar=diar+arr[i][j];
        dif=abs(dial-diar);     
    return dif;

if __name__ == '__main__':
    n = int(input());
    arr = [];
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())));

    result = diagonalDifference(arr);

    print(result);

/*
Input:
3
11 2 4
4 5 6
10 8 -12

Output:
15
*/
