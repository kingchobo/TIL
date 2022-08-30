import sys
n = int(sys.stdin.readline().strip())
cnt = 0

# 재귀 함수
def fib(n):
    global cnt
    if n == 1 or n == 2:
        cnt += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(n)
print(cnt, end=' ')

# DP
def fibo(n):
    global cnt
    arr = [0, 1, 1]
    for i in range(3, n+1):
        arr.append(arr[i-1] + arr[i-2])
        cnt += 1
    return arr[n]

cnt = 0
fibo(n)
print(cnt)