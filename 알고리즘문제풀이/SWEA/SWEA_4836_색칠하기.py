T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    purple = 0
    arr1 = []   # 1색을 담을 리스트
    arr2 = []   # 2색을 담을 리스트

    # 색깔별로 나누기
    for n in range(N):
        if arr[n][-1] == 1:
            arr1.append(arr[n])
        else:
            arr2.append(arr[n])
    # 서로 다른 색에 대하여 겹치는 부분의 넓이 구하기
    for i in arr1:
        for j in arr2:
            x = set(range(i[0], i[2]+1)) & set(range(j[0], j[2]+1))
            y = set(range(i[1], i[3]+1)) & set(range(j[1], j[3]+1))
            purple += len(x) * len(y)

    print(f'#{tc} {purple}')