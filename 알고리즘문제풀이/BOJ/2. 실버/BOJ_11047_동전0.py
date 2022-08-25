import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

num = 0
for i in arr[::-1]:
    temp = k // i
    num += temp
    k -= temp * i

print(num)