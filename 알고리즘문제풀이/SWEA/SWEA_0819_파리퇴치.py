T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    # 매 번 잡히는 파리수 중 최대값을 저장할 변수 선언
    max_sum = 0

    # N-M까지의 영역을 파리채 범위만큼씩 순회하며 잡는 파리수를 sum에 저장 후,
    # sum과 max_sum을 비교하여 max_sum 값을 최신화
    for l in range(N-M+1):
        for m in range(N-M+1):
            sum = 0
            for i in range(M):
                for j in range(M):
                    sum += area[l+i][m+j]
            if sum > max_sum:
                max_sum = sum

    print(f'#{tc} {max_sum}')