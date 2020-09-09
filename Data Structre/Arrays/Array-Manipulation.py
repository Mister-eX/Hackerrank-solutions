
import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    L=[0]*n
    for qr in queries:
        L[qr[0]-1]+= qr[2]
        if qr[1]!=n:
            L[qr[1]]-=qr[2]
    temp=0
    max_value=0
    for i in L:
        temp+=i
        if temp>max_value:
            max_value= temp
    return max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
