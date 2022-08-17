arr = list(input())
stack = []
operators = ('+', '-', '*', '/')
for i in range(len(arr)):
    if arr[i] in operators:
        num1 = stack.pop()
        num2 = stack.pop()
        if arr[i] == '+':
            stack.append(num1 + num2)
        elif arr[i] == '-':
            stack.append(num2 - num1)
        elif arr[i] == '*':
            stack.append(num1 * num2)
        else:
            stack.append(num2 // num1)
    else:
        stack.append(int(arr[i]))

print(stack[0])