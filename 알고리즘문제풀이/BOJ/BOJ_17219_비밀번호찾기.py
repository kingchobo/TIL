import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = {}
for i in range(n):
    a, b = input().split()
    arr[a] = b

for i in range(m):
    site = input().strip()
    print(arr[site])