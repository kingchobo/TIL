t = int(input())
for tc in range(1, t+1):
    n, p = map(int, input().split())
    arr = [[1] for _ in range(p)]    # 묶음의 수 만큼은 나뉘어져야 하므로 1씩 넣어둔다.
    n -= p    # 넣은 만큼 n에서 빼준다.

    # 서로 곱해지는 수들의 크기가 비슷할 수록 곱이 커지므로 최대한 균등하게 나눈다.
    temp_1 = n // p
    for i in arr:
        i[0] += temp_1

    # 나머지를 1씩 균등하게 분배
    temp_2 = n % p
    j = 0
    while temp_2 > 0:
        arr[j % p][0] += 1
        temp_2 -= 1
        j += 1

    # ans에 모든 수들을 곱해준 후 출력
    ans = 1
    for i in arr:
        ans *= i[0]
    print(f'#{tc} {ans}')