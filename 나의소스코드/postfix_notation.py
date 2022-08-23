# 문자열 수식을 리스트로 받아서 후위표기법으로 바꾸는 함수
def postfix_notation(arr):
    N = len(arr)
    priority = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    postfix = []
    stack = []
    for i in range(N):
        if arr[i].isdigit():
            postfix.append(arr[i])
        elif arr[i] == '(':
            stack.append(arr[i])
        elif arr[i] == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and priority[arr[i]] <= priority[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(arr[i])

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)