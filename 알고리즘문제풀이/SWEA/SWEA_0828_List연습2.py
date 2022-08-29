t = int(input())
for tc in range(1, t+1):
    # 부분집합 subset 만들기
    given_set = set(map(int, input().split()))
    subset = [[]]
    for num in given_set:
        size = len(subset)
        for i in range(size):
            subset.append(subset[i] + [num])

    # 공집합을 제외한 모든 부분집합에서 합이 0인경우가 있는지 확인
    for i in subset[1:]:
        if sum(i) == 0:
            print(f'#{tc} 1')
            break
    else:
        print(f'#{tc} 0')