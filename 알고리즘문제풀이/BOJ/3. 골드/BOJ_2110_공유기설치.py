from itertools import combinations
import sys

n, c = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()

my_max = 0
for i in combinations(arr, c):
    my_min = 200001
    for j in range(c-1):
        m = abs(i[j] - i[j+1])
        if m < my_min:
            my_min = m
    if my_min > my_max:
        my_max = my_min
    if my_max >= abs(arr[0]-arr[-1]) // c + 1:
        break

print(my_max)