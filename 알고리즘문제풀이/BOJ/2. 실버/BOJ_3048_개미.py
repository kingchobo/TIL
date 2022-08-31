n1, n2 = map(int, input().split())
arr1 = list(input())
arr2 = list(input())
t = int(input())

R = []
L = []
for i in arr1[::-1]:
    R.append((i, 'r'))
for i in arr2:
    L.append((i, 'l'))

ans = R + L
for _ in range(t):
    idx = 0
    while idx <= n1 + n2 - 2:
        if ans[idx][1] == 'r' and ans[idx+1][1] == 'l':
            ans[idx], ans[idx+1] = ans[idx+1], ans[idx]
            idx += 2
        else:
            idx += 1

for i in range(n1 + n2):
    print(ans[i][0], end='')