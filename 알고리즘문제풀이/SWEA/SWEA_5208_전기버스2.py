T = int(input())
for TC in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    stops = arr[1:] + [0]

    cur = 0
    cnt = 0
    while True:
        if stops[cur] == 1:
            cur += 1
            cnt += 1
        else:
            temp_max = temp_idx = 0
            for i in range(cur+1, cur + stops[cur]+1):
                if i + stops[i] > temp_max:
                    temp_max = i + stops[i]
                    temp_idx = i
            cur = temp_idx
            cnt += 1

        if cur >= N-1 or cur + stops[cur] >= N-1:
            break
    print(f'#{TC} {cnt}')