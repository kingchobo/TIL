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

    if len(stack) == 1:
        return stack[-1]
    else:
        return 'error'

T = int(input())
for tc in range(1, T+1):
    try:
        arr = list(input().split())
        arr.pop()
        ans = calc_postfix(arr)
        print(f'#{tc} {ans}')
    except:
        print(f'#{tc} error')