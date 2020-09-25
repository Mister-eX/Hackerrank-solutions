def largest_rectangle(h):
    largest = 0
    stack = deque()
    i = 0
    n = len(h)

    while i < n:
        if (not stack) or (h[i] >= h[stack[-1]]):
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            if stack:
                size = h[top] * (i - stack[-1] -1)
            else:
                size = h[top] * i
            if size > largest:
                largest = size

    while stack:
        top = stack.top()
        if stack:
            size = h[top] * (n - stack[-1] -1)
        else:
            size = h[top] * n
        if size > largest:
            largest = size

    return largest
         