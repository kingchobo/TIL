from itertools import permutations
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
arr2 = list(permutations(arr, m))
for i in range(len(arr2)):
    print(*arr2[i])