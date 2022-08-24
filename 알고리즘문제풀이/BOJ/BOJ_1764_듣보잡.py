import sys
input = sys.stdin.readline

n, m = map(int, input().split())
set1 = set()
set2 = set()

for i in range(n):
    set1.add(input().strip())
for i in range(m):
    set2.add(input().strip())

arr = list(set1 & set2)
num = len(arr)
arr.sort()
print(num)
for i in range(num):
    print(arr[i])