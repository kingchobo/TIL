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

# 후위표기법으로 표기된 리스트 수식을 받아서 연산하는 함수
def calc_postfix(arr):
    N = len(arr)
    operators = ['*', '/', '+', '-']
    stack = []

    for i in range(N):
        if arr[i].isdigit():
            stack.append(int(arr[i]))
        elif arr[i] == '+':
            temp_2 = stack.pop()
            temp_1 = stack.pop()
            stack.append(temp_1 + temp_2)
        elif arr[i] == '-':
            temp_2 = stack.pop()
            temp_1 = stack.pop()
            stack.append(temp_1 - temp_2)
        elif arr[i] == '*':
            temp_2 = stack.pop()
            temp_1 = stack.pop()
            stack.append(temp_1 * temp_2)
        elif arr[i] == '/':
            temp_2 = stack.pop()
            temp_1 = stack.pop()
            stack.append(temp_1 // temp_2)

    return stack[-1]

T = 10
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {calc_postfix(postfix_notation(input()))}')