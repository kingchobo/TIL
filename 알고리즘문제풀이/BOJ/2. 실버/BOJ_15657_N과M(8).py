from itertools import product
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
arr2 = list(product(arr, repeat=m))
for i in range(len(arr2)):
    print(*arr2[i])