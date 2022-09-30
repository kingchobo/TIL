def is_possible(chess, i, j):
    for k in range(3):
        for t in range(1, N):
            ni = i + di[k] * t
            nj = j + dj[k] * t
            if 0 <= ni < N and 0 <= nj < N:
                if chess[ni][nj] == 1:
                    return False
    return True


def queen(chess, i):
    global ans
    if i == N:
        ans += 1
        return
    for j in range(N):
        if is_possible(chess, i, j):
            chess[i][j] = 1
            queen(chess, i+1)
            chess[i][j] = 0


T = int(input())
for TC in range(1, T+1):
    N = int(input())
    ans = 0
    chess_board = [[0]*N for _ in range(N)]
    # 상, 우상, 좌상
    di = [-1, -1, -1]
    dj = [0, 1, -1]
    queen(chess_board, 0)
    print(f'#{TC} {ans}')