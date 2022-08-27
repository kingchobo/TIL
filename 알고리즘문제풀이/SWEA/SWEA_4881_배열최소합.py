def f(i, s):
    global min_v
    if i == n:
        if min_v > s:
            min_v = s
    else:
        for j in range(i, n):
            p[i], p[j] = p[j], p[i]
            f(i+1, s+area[i][p[i]])
            p[i], p[j] = p[j], p[i]


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    area = [list(map(int, input().split())) for _ in range(n)]

    p = [i for i in range(n)]
    min_v = 1000
    f(0, 0)
    print(f'#{tc} {min_v}')