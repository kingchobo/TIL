T = int(input())
for _ in range(T):
    n, idx = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = [[0]]*n

    for i in range(n):
        queue[i] = [0, arr[i]]
    queue[idx][0] = 'idx'

    cnt = 1
    while True:
        if n == 1:
            print(cnt)
            break
        for i in range(1, n):
            if queue[0][1] < queue[i][1]:
                queue.append(queue.pop(0))
                break
        else:
            a = queue.pop(0)
            if a[0] == 'idx':
                print(cnt)
                break
            n -= 1
            cnt += 1