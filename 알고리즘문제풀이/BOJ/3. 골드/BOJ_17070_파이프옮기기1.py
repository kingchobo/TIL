import sys

N = int(input())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp_horizontal = [[0] * N for _ in range(N)]
dp_vertical = [[0] * N for _ in range(N)]
dp_diagonal = [[0] * N for _ in range(N)]

dp_horizontal[0][1] = 1

for i in range(N):
    for j in range(N):
        if dp_horizontal[i][j]:
            if j + 1 < N and area[i][j+1] == 0:
                dp_horizontal[i][j+1] += dp_horizontal[i][j]
                if i + 1 < N and area[i+1][j] == area[i+1][j+1] == 0:
                    dp_diagonal[i+1][j+1] += dp_horizontal[i][j]

        if dp_vertical[i][j]:
            if i + 1 < N and area[i+1][j] == 0:
                dp_vertical[i+1][j] += dp_vertical[i][j]
                if j + 1 < N and area[i][j+1] == area[i+1][j+1] == 0:
                    dp_diagonal[i+1][j+1] += dp_vertical[i][j]

        if dp_diagonal[i][j]:
            cnt = 0
            if j + 1 < N and area[i][j+1] == 0:
                dp_horizontal[i][j+1] += dp_diagonal[i][j]
                cnt += 1
            if i + 1 < N and area[i+1][j] == 0:
                dp_vertical[i+1][j] += dp_diagonal[i][j]
                cnt += 1
            if cnt == 2 and area[i+1][j+1] == 0:
                dp_diagonal[i+1][j+1] += dp_diagonal[i][j]

print(dp_diagonal[N-1][N-1] + dp_horizontal[N-1][N-1] + dp_vertical[N-1][N-1])