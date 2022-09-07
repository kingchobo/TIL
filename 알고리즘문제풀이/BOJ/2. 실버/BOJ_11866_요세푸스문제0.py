n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
ans = [arr[k-1]]
arr[k-1] = 0
i = k-1
while len(ans) != n:
    cnt = 0
    while cnt != k:
        if i == len(arr)-1:
            i = 0
        else:
            i += 1
        if arr[i] != 0:
            cnt += 1
    ans.append(arr[i])
    arr[i] = 0

print('<', end='')
for i in ans[:-1]:
    print(i, end=', ')
print(ans[-1], end='')
print('>')