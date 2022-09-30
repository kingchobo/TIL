import sys
from sys import setrecursionlimit
setrecursionlimit(10000000)


def union(v1, v2):
    a = find_set(v1)
    b = find_set(v2)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


def find_set(v):
    if arr[v] != v:
        arr[v] = find_set(arr[v])
    return arr[v]


n, m = map(int, sys.stdin.readline().split())        # n = 가장 큰 자연수, m = 연산의 개수
arr = [i for i in range(n+1)]

for _ in range(m):
    c, a, b = map(int, sys.stdin.readline().split())
    if c == 0:
        union(a, b)
    else:
        if find_set(b) == find_set(a):
            print('yes')
        else:
            print('no')