import sys
# test case의 개수 t
t = int(sys.stdin.readline())
for _ in range(t):
    # 쓰레기차의 용량 W, 방문해야 할 지점의 수 N
    W, N = map(int, sys.stdin.readline().split())

    # 각 지점들의 정보(거리, 쓰레기양)를 저장할 리스트 places
    # places[0]은 쓰레기장, total = 총 쓰레기 양
    places = [[0, 0]] * (N+1)
    # total = 0
    for i in range(1, N+1):
        x, w = map(int, sys.stdin.readline().split())
        places[i] = [x, w]
        # total += w

    v = 0           # 현재 쓰레기차에 실려있는 쓰레기의 용량
    idx = 0         # 방문할 지점의 인덱스
    distance = 0    # 쓰레기차가 이동한 거리
    while True:
        idx += 1
        distance += places[idx][0] - places[idx-1][0]
        # 종료조건 : 끝 지점에 도달했을 때 아래 두 가지 경우에 따라 distance만 조절
        if idx == N:
            if v + places[idx][1] <= W:
                distance += places[idx][0]
                break
            else:
                distance += places[idx][0] * 3
                break
        # 세 가지 경우
        if v + places[idx][1] < W:
            v += places[idx][1]
        elif v + places[idx][1] == W:
            v += places[idx][1]
            distance += places[idx][0] * 2
            # places[0][1] += v
            v = 0
        else:
            distance += places[idx][0] * 2
            # places[0][1] += v
            v = 0
            v += places[idx][1]

    print(distance)