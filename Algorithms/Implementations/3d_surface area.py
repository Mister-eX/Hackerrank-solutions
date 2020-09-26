def surfaceArea(arr, R, C):
    fc= 2*R*C
    top= 0
    side= 0
    if R==1 and C==1:
        return fc+4*arr[0][0]
    
    for i in range(R):
            for j in range(C):
                if i==0 or j==C-1 or i==R-1 or j==0:
                    side+=arr[i][j]
    
    if R>1 and C>1:
        side+=(arr[0][0]+arr[0][C-1]+arr[R-1][0]+arr[R-1][C-1])
        for i in range(R-1):
            for j in range(C-1):
                top+=abs(arr[i][j]-arr[i][j+1])
                top+=abs(arr[i][j]-arr[i+1][j])
            top+=abs(arr[i][C-1]-arr[i+1][C-1])
        for j in range(C-1):
            top+=abs(arr[R-1][j]-arr[R-1][j+1])
    
    if R>1 and C==1:
        side=side*2
        side+=(arr[0][0]+arr[R-1][0])
        for i in range(R-1):
            top+=abs(arr[i][0]-arr[i+1][0])
    
    if R==1 and C>1:
        side=side*2
        side+=(arr[0][0]+arr[0][C-1])
        for i in range(C-1):
            top+=abs(arr[0][i]-arr[0][i+1])

    return (fc+top+side)

