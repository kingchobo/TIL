str_1 = input()
str_2 = input()
L1 = len(str_1)
L2 = len(str_2)

dp = [[0] * L2 for _ in range(L1)]

for i in range(L1):
    for j in range(L2):
        if str_1[i] == str_2[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1

print(max(map(max, dp)))