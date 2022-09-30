t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())              # n: 컨테이너의 수, m: 트럭의 수
    containers = list(map(int, input().split()))  # 컨테이너들의 무게를 저장한 리스트
    trucks = list(map(int, input().split()))      # 트럭들의 적재 용량을 저장한 리스트

    total_weight = 0

    while containers and trucks:  # 트럭이나 화물 중 하나라도 동나면 종료
        # [1] 가장 무거운 화물과 가장 큰 트럭을 꺼내서 비교
        # [2-1] 실을 수 있으면 total_weight에 추가.
        # [2-2] 실을 수 없으면 그 화물은 포기하고 트럭은 다시 트럭리스트에 넣기
        heaviest = containers.pop(containers.index(max(containers)))
        biggest = trucks.pop(trucks.index(max(trucks)))
        if heaviest <= biggest:
            total_weight += heaviest
        else:
            trucks.append(biggest)

    print(f'#{tc} {total_weight}')