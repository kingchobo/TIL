def times(P, f):
    cnt = 0
    l = 1
    r = P
    while True:
        c = int((l+r) / 2)
        if c == f:
            break
        elif c > f:
            r = c
            cnt += 1
        else:
            l = c
            cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    if times(P, A) > times(P, B):
        print(f'#{tc} B')
    elif times(P, A) < times(P, B):
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')