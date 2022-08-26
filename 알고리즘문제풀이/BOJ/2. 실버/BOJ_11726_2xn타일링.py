n = int(input())
ans = [1, 2]
if n == 1:
    print(ans[0])
elif n == 2:
    print(ans[1])
else:
    for i in range(2, n):
        ans.append(ans[i-1] + ans[i-2])
    print(ans[-1]%10007)