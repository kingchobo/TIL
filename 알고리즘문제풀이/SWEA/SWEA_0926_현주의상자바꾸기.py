T = int(input())
for TC in range(1, T+1):
    N, Q = map(int, input().split())
    boxes = [0] * (N+1)
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            boxes[j] = i
    print(f'#{TC}', *boxes[1:])