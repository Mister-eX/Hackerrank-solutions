import math
from collections import deque

def encryption(s):
    n= len(s)
    x = math.sqrt(n)
    r = math.floor(x)
    c = math.ceil(x)
    if r * c < n:
        r += 1
    for i in range(c):
        j = i
        while j < n:
            string = string + s[j]
            j += c
        string = string + ' '
    return string