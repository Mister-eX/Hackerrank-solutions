from collections impprt Counter
def isValid(string):
    dict1 = Counter(string)
    dict2 = {}
    min_count = sys.maxsize
    max_count = -sys.maxsize

    for element, freq in dict1.items():
        if freq in dict2:
            dict2[freq] += 1
        else:
            dict2[freq] = 1

        if freq > max_count:
            max_count = freq
        
        if freq < min_count:
            min_count = freq

    if len(dict2) == 1:
        return "YES"
        
    elif len(dct2) == 2:
        if dict2[max_count] == 1 and max_count - min_count ==1:
            return "YES"
        elif dict2[min_count] == 1 and min_count == 1:
            return "YES"
    return "NO"


