def maximumToys(prices, k):
    prices.sort()
    i = 0
    while k >0:
        if k > prices[i]:
            k -= prices[i]
            i += 1
        else:
            break
    
    return i