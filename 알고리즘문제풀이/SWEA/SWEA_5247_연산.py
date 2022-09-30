T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())        # N: 주어진 자연수, M: 만들 자연수
    arr = [1, -1, 0, -10]       # 문제에서 주어진 연산 종류. 0이 나오면 *2를 해준다.

    Q = []
    visited = [0] * 1000001
    visited[N] = 1
    Q.append((N, 0))
    done = False
    cnt = 0

    while not done:
        cur, cnt = Q.pop(0)
        for i in arr:
            if i:
                temp = cur + i
            else:
                temp = cur * 2

            if 0 <= temp <= 1000000:
                if not visited[temp]:
                    visited[temp] = 1
                    Q.append((temp, cnt+1))

            if temp == M:
                done = True
                break

    print(f'#{TC} {cnt+1}')