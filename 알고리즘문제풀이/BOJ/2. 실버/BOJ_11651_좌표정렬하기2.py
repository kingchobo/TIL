import sys
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split()))[::-1] for _ in range(n)]
arr.sort()
for i in arr:
    print(*i[::-1])