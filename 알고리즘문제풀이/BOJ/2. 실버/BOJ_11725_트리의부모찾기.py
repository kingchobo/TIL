import sys
sys.setrecursionlimit(100000000)


def f(num):
    visited[num] = 1
    for nod in arr[num]:
        if not visited[nod]:
            ans[nod] = num
            f(nod)


N = int(sys.stdin.readline())
arr = [[] for _ in range(N+1)]
ans = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [0] * (N+1)
visited[1] = 1
for i in arr[1]:
    ans[i] = 1
    f(i)

for i in range(2, N+1):
    print(ans[i])