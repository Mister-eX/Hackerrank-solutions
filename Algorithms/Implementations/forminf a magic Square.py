def formingMagicSquare(s):
    magic_square = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
               [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
               [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
               [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
               [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
               [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
               [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
               [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]

    min_v= 100
    for mat in magic_square:
        count= 0
        for i in range(3):
            for j in range(3):
                if s[i][j]!=mat[i][j]:
                    count += abs(s[i][j] - mat[i][j])
        if count < min_v:
            min_v= count

    return min_v
