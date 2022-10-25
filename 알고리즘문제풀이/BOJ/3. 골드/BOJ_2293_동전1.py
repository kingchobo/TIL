N, K = map(int, input().split())

nums_list = [0] * N
for i in range(N):
    nums_list[i] = int(input())

dp = [0] * (K+1)
dp[0] = 1
for i in nums_list:
    for j in range(K+1):
        if i <= j:
            dp[j] = dp[j] + dp[j-i]

print(dp[-1])