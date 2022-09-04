import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    k, v = sys.stdin.readline().split()
    arr.append((int(k), i, v))
arr.sort()
for i in range(n):
    print(arr[i][0], arr[i][2])