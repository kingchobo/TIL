import sys

n = int(sys.stdin.readline())
num_list = [0] * n

for i in range(n):
    num_list[i] = int(sys.stdin.readline())

# 산술평균
avg = sum(num_list) / n
print(f'{avg:.0f}')

# 중앙값
num_list.sort()
if n % 2 == 0:
    mid = (num_list[n//2 - 1] + num_list[n//2]) / 2
else:
    mid = num_list[n//2]
print(mid)

# 최빈값
counts = dict()
for i in range(1, n+1):
    counts[i] = []
maxCount = 1
count = 1
for i in range(1, n):
    if num_list[i] == num_list[i-1]:
        count += 1
    else:
        counts[count].append(num_list[i-1])
        if maxCount < count: maxCount = count
        count = 1
    if i == n-1:
        counts[count].append(num_list[i])
        if maxCount < count: maxCount = count

# 범위
print(abs(num_list[-1] - num_list[0]))