n = int(input())
a = list(map(int, input().split()))
ans = [0] * n


for i in range(n):
    ans[i] = 1
    for j in range(0, i):
        if a[j] < a[i] and ans[i] < ans[j] + 1:
            ans[i] = ans[j] + 1

print(max(ans))