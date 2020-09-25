from collections import deque

def text_editor(queries):
    undo = deque()
    string = ''
    n= 0
    for Q i in queries:
        if Q[0] == '1':
            string += Q[1]
            n += len(Q[1])
            undo.appendleft(['append', Q[1]])
            continue
        if Q[0] == '2':
            temp = string[n - int(Q[1]): ]
            string = string[: n - int(Q[1])] + ''
            n -= int(Q[1])
            undo.appendleft(['delete', temp])
            continue
        if Q[0] == '3':
            print(string[int(Q[1])-1])
            continue
        if Q[0] == '4':
            if undo[0][0] == 'append':
                x = len(undo[0][1])
                string = string[ : n - x] + ''
                n -= x
                undo.popleft()
                continue
            if undo[0][0] == 'delete':
                string = string + undo[0][1]
                n += len(undo[0][1])
                undo.popleft()
                continue
