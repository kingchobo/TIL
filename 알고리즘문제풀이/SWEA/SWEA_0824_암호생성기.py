t = 10
for _ in range(t):
    tc = int(input())
    arr = list(map(int, input().split()))
    n = 1
    while True:
        if n == 6:
            n = 1
        if arr[0] - n > 0:
            arr.append(arr.pop(0) - n)
            n += 1
        else:
            arr.append(0)
            del arr[0]
            break

    print(f'#{tc}', end = ' ')
    print(*arr)