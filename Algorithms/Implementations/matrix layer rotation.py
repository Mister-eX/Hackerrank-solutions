#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    output = [[0 for j in range(n)] for i in range(m)]

    k = min(m, n)//2
    for x in range(k):
        size = 2*(m+n - 4*x -2)
        temp =[0 for _ in range(size)]
        index = 0
        top = x
        bottom = m- x-1
        left= x
        right = n-x-1
        print(top, right, bottom, left)
        for topi in range(top , right +1):
            temp[(index -r)%size] = matrix[top][topi]
            index += 1
            
        for righti in range(top+1, bottom):
            temp[(index -r )%size] = matrix[righti][right]
            index += 1
        
        for bottomi in range(right, top-1, -1):
            temp[(index -r)%size]= matrix[bottom][bottomi]
            index += 1
        
        for lefti in range(bottom -1,top, -1):
            temp[(index - r)%size] = matrix[lefti][left]
            index += 1
        print(temp)
        index = 0
        for topi in range(top , right +1):
            output[top][topi] = temp[index]
            index += 1
            
        for righti in range(top+1, bottom):
            output[righti][right] = temp[index]
            index += 1
        
        for bottomi in range(right, top-1, -1):
            output[bottom][bottomi] = temp[index]
            index += 1
        
        for lefti in range(bottom -1,top, -1):
            output[lefti][left] = temp[index]
            index += 1

        for i in range(m):
            print(' '.join(map(str, output[i])))


if __name__ == '__main__':
    '''matrix = [[2, 3, 4, 8], 
             [1, 7, 11, 12],
             [5, 6, 10, 16],
             [9, 13, 14, 15]]'''
    matrix = [[1, 2, 3, 4], 
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
    
    matrixRotation(matrix, 1)
