A = {i for i in range(1,13)}

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    subset = [[]]
    for num in A:
        size = len(subset)
        for y in range(size):
            subset.append(subset[y] + [num])
    cnt = 0
    for i in subset:
        if len(i) == N:
            sum = 0
            for j in i:
                sum += j
            if sum == K:
                cnt +=1
    print(f'#{tc} {cnt}')