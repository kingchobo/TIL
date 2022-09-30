import sys

n = int(sys.stdin.readline())
pole = [[0, 0]] * n

dp = [0] * n
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    pole[i] = [a, b]
pole.sort()

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if pole[i][1] > pole[j][1] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(n - max(dp))