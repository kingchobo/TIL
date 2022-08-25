import sys
input = sys.stdin.readline

n = int(input())
ans = [0] * (n+1)
stairs = [0]
for _ in range(n):
    stairs.append(int(input().strip()))

ans[1] = stairs[1]

for i in range(2, n+1):
    ans[i] = max(stairs[i-1] + ans[i-3], ans[i-2]) + stairs[i]

print(ans[n])