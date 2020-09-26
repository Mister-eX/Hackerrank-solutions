def biggerIsGreater(w):
    n= len(w)
    w= list(w)
    i=n-1
    l=[]
    j=0
    flag= False
    while(i>0):
        if w[i-1]<w[i]:
            flag= True
            break
        i-=1
    if flag== False:
        return "no answer"
    else:
        j=n-1
        while(j>=i):
            if w[j]>w[i-1]:
                break
            j-=1

        w[i-1], w[j]= w[j], w[i-1]

        m=i
        while(i<n):
            l.append(w[i])
            i+=1
        l.sort()
    return (''.join(w[:m])+''.join(l))

