from collections import Counter

def sherlockAndAnagrams(s):
    n = len(s)
    dict1 = {}
    for i in range(n):
        for j in range(n-i):
            s1 = ''.join(sorted(s[j: j + i +1]))
            dict1[s1] = dict1.get(s1, 0) + 1
    for key in dict1:
        count += dict1[key] * (dict1[key] - 1)//2
    return count