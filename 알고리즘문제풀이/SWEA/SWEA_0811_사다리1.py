for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for __ in range(100)]
    x, y = 99, 99
    for i in range(100):
        if arr[x][i] == 2:
            x -= 1
            y = i
            break
    while True:
        if x == 0:
            break

        if y != 0 and arr[x][y-1] == 1:
            arr[x][y] = 0
            y -= 1

        elif y != 99 and arr[x][y+1] == 1:
            arr[x][y] = 0
            y += 1

        else:
            x -= 1

    print(f'#{tc} {y}')