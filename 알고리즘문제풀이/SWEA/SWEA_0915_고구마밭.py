T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    # long은 긴줄기들을 담을 리스트
    # temp에 맨 왼쪽 밭의 고구마 넣어놓고 시작
    long = []
    temp = [arr[0]]
    
    for i in range(1, n):
        # temp에 들어있는 마지막 고구마(바로 왼쪽)보다 크면 추가
        if arr[i] > temp[-1]:
            temp.append(arr[i])
        # 아닐경우, temp의 길이가 2 이상이면 긴줄기 이므로 long에 추가
        # 이후 temp를 현재 인덱스의 고구마양으로 초기화
        else:
            if len(temp) >= 2:
                long.append(temp)
            temp = [arr[i]]
    if len(temp) >= 2:
        long.append(temp)
    
    # 긴 줄기가 하나라도 있으면
    if len(long) > 0:
        len_of_long = []     # 각 긴줄기들의 길이를 저장
        sum_of_longest = []  # 가장 긴 긴줄기들의 고구마 개수를 저장
        # 긴줄기의 길이 저장
        for i in long:
            len_of_long.append(len(i))
        
        for i in range(len(len_of_long)):
            if len_of_long[i] == max(len_of_long):  # 가장 긴 긴줄기면, 고구마 개수 저장 
                sum_of_longest.append(sum(long[i]))
                
        print(f'#{tc} {len(long)} {max(sum_of_longest)}')

    # 긴 줄기가 없으면
    else:
        print(f'#{tc} 0 0')