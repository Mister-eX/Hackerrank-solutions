from collections import deque

def isBalancedBrackets(string):
    stack = deque()
    for ele in string:
        if ele == '(' or ele == '{' or ele == '[':
            stack.append(ele)
            continue

        if stack:
            if ele == ')' and stack[-1] == '(':
                stack.pop()
                continue

            if ele == '}' and stack[-1] == '{':
                stack.pop()
                continue

            if ele == ']' and stack[-1] == '[':
                stack.pop()
                continue

        return "NO"

    if stack:
        return "NO"
    else:
        return "YES"


if __name__=="__main__":
    string = "{)[](}]}]}))}(())("
    print(isBalancedBrackets(string))