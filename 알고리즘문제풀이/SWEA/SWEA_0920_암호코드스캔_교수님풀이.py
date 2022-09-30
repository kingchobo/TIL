pat = {211: 0, 221: 1, 122: 2, 411: 3, 132: 4,
       231: 5, 114: 6, 312: 7, 213: 8, 112: 9}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    arrb = [[0] * (M*4) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            h = int(arr[i][j], 16)           # 16진수 문자열 -> 정수
            for k in range(4):
                if h & (1 << (3-k)):         # [0] - [3] -> b3 ~ b0
                    arrb[i][j*4 + k] = 1
                else:
                    arrb[i][j*4 + k] = 0

    ans = 0
    M *= 4
    for i in range(N):
        # for j in range(M-55):    # 1 or 0이 56개는 남아 있어야 탐색하는 의미가 있음
        j = 0
        k = 0
        while k < 8 and j < M - 55:
            code = [0] * 8
            a = b = c = 0
            while arrb[i][j] == 0 and j < M-55:
                j += 1
            if j == M - 55:
                break
