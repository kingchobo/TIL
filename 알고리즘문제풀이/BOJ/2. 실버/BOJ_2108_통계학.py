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
count_num = {}
for i in num_list:
    if i not in count_num:
        count_num[i] = 1
    else:
        count_num[i] += 1

