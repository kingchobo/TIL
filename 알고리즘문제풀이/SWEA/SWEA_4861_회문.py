T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 가로 찾기
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if arr[i][j:j+M][k] != arr[i][j:j+M][-1-k]:
                    break
            else:
                print(f"#{tc} {''.join(arr[i][j:j+M])}")

    # 세로 찾기
    for k in range(N):
        for i in range(N-M+1):
            for j in range(M//2):
                if arr[i+j][k] != arr[i+M-j-1][k]:
                    break
            else:
                ans = [arr[i+j][k] for j in range(M)]
                print(f"#{tc} {''.join(ans)}")

