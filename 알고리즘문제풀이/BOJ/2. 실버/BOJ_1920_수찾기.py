import sys

n = int(sys.stdin.readline().strip())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()

m = int(sys.stdin.readline().strip())
m_list = list(map(int, sys.stdin.readline().split()))


def binary(target):
    left = 0
    right = n-1

    while left <= right:
        mid = (left + right) // 2
        if n_list[mid] == target:
            return True

        if target < n_list[mid]:
            right = mid - 1

        elif target > n_list[mid]:
            left = mid + 1


for i in range(m):
    if binary(m_list[i]):
        print(1)
    else:
        print(0)