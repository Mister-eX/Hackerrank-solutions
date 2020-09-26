def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)), reverse= True)
    result = []
    for a in alice:
        n = len(scores)
        if a > scores[0]:
            scores.insert(0, a)
            result.append(1)
        elif a < scores[n-1]:
            score.append(a)
            result.append(n+1)
        else:
            first = 0
            last = n - 1
            while first <= last:
                mid = (first + last)//2
                if scores[mid] == a:
                    result.append(mid + 1)
                    break
                elif scores[mid] > a:
                    if mid + 1 < n:
                        if scores[mid + 1] < a:
                            scores.insert(mid + 1, a)
                            result.append(mid + 2)
                            break
                    first = mid + 1
                else:
                    last = mid - 1
    return result