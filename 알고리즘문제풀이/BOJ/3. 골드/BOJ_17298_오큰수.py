import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
ans = [-1] * N
stack = [0]

for i in range(1, N):
    while stack and arr[i] > arr[stack[-1]]:
        ans[stack.pop()] = arr[i]
    stack.append(i)

for j in ans:
    print(j, end=' ')