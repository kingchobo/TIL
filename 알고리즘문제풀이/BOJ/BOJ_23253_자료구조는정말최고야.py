N, M = map(int, input().split())

arr = []
for _ in range(M):
    k = int(input())
    arr.append(list(map(int, input().split())))

i = 1
check = 0
while True:
    if i == N:
        print('Yes')
        break
    if check < 0:
        print('No')
        break
    for j in range(M):
        if len(arr[j]) and arr[j][-1] == i:
            arr[j].pop()
            i += 1
            break
    else:
        check -= 1