import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum_arr = [0]
temp = 0
for k in arr:
    temp += k
    sum_arr.append(temp)

for _ in range(m):
    i, j = map(int, input().split())
    print(sum_arr[j] - sum_arr[i-1])