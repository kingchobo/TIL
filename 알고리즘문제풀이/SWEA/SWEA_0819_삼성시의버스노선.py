T = int(input())
for tc in range(1, T+1):
    # 이하 인풋 정리
    # N = 버스 노선의 개수
    # line_list = 버스 노선 기점과 종점을 담은 리스트
    # P = 문제에서 확인할 버스 정류장의 개수
    # bus_stop_list = P개의 버스 정류장의 번호
    # total_bus_stop = 5,000개의 총 버스 정류장 리스트(초기값 = 0)
    N = int(input())
    line_list = []
    for _ in range(N):
        s, e = map(int, input().split())
        line_list.append((s, e))
    P = int(input())
    total_bus_stop = [0] * 5001
    bus_stop_list = []
    for _ in range(P):
        bus_stop_list.append(int(input()))

    # 버스노선의 기점과 종점의 range에 속하는 버정들을 전부 +1
    for i in line_list:
        for j in range(i[0], i[1]+1):
            total_bus_stop[j] += 1
    print(f'#{tc}', end=' ')
    for k in bus_stop_list:
        print(total_bus_stop[k], end=' ')
    print()
