def gridSearch(G, P, R, C, r, c):
    for i in range(R-r+1):
        for j in range(C-c+1):
            if G[i][j]==P[0][0]:
                found=True
                for i1 in range(r):
                    if P[i1][0:c]!=G[i+i1][j:j+c]:
                        found=False
                        break
                if found==True:
                    return "YES"
    return "NO"