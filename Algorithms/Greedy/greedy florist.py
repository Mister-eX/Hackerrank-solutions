def getMinimumCost(org_price, k):
    n = len(org_price) - 1
    org_price.sort()
    ans =0 
    count = 0
    while n >= 0:
        i = k
        while i > 0:
            x = org_price[n] * (count + 1)
            n -= 1
            ans += x
            i -= 1
            if n <0:
                return ans
            
        count += 1
    
    return ans