def queensAttack(n, k, r_q, c_q, obstacles):
     R= n-r_q #right position
    L= r_q -1 #left position
    U= n- c_q #up
    D= c_q-1 #down
    UL= min(r_q -1, n- c_q) #up-left
    UR= min(n- r_q, n-c_q) #up-right
    DL= min(r_q -1, c_q -1) #down-left
    DR= min(n- r_q, c_q-1) #down-right

    for x, y in obstacles:
        if x==r_q:#up or down
            if y > c_q:#up
                U= min(y-c_q-1, U)
            if y< c_q: #down
                D= min(c_q-y-1, D)
        if y== c_q: #left or right
            if x> r_q: #right
                R= min(x-r_q-1, R)
            if x< r_q: #left
                L= min(r_q-x-1, L)
        if abs(x- r_q)==abs(y-c_q): #diagonals 
            if y> c_q: #up-diagonals
                if x< r_q: #up-left diagonals
                    UL= min(r_q- x-1, UL)
                if x> r_q: #up-right
                    UR= min(x- r_q-1, UR)
            if y< c_q: #down-diagonals
                if x< r_q: #down-left 
                    DL= min(r_q-x-1, DL)
                if x> r_q: #down-right
                    DR= min(x-r_q-1, DR)
    return (U+D+R+L+UR+UL+DR+DL)