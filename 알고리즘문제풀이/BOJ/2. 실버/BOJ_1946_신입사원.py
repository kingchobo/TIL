import sys

t = int(sys.stdin.readline())
for tc in range(t):
    n = int(sys.stdin.readline())
    arr = [0] * (n + 1)
    for _ in range(n):
        paper, interview = map(int, sys.stdin.readline().split())
        arr[paper] = interview
    compare_idx = 1
    cnt = 0
    for i in range(2, n + 1):
        if arr[i] > arr[compare_idx]:
            cnt += 1
        else:
            compare_idx = i

    print(n - cnt)