N, M = map(int, input().split())
arr = [map(int, input().split())]
sum = 0
L = len(arr)
for i in range(L-2):
    for j in range(1,L-1):
        for k in range(2,L):
            if (arr[i]+arr[j]+arr[k]) < M and (arr[i]+arr[j]+arr[k]) > sum:
                sum = arr[i]+arr[j]+arr[k]
print(sum)