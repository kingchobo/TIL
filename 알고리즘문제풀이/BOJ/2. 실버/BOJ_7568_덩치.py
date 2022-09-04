import sys
n = int(sys.stdin.readline())
arr = []
rank_list = [1] * n
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x, y))
for i in range(n):
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank_list[i] += 1
print(*rank_list)