import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
bat = [2]  # 매 회차마다 배터리 소모량 저쟝
ans = 2    # 현재 에어팟의 누적 배터리 소모량
idx = 1    # 인덱스 1부터 탐색
while idx <= n-1:
    if arr[idx] != arr[idx-1]:  # 앞의 핸드폰과 다르면
        bat.append(2)           # 2% 소모한거 저장
        ans += 2                # 누적 += 2
    else:                       
        temp = bat[-1] * 2      # 연산 두 번 하지 말라고 temp에 저장
        bat.append(temp)        # 직전 소모량의 2배값 저장
        ans += temp             # 누적에 합산
    if ans >= 100 and idx != n-1:    # 누적이 100 이상이 되면
        idx += 1                     # 그 다음 핸드폰으로 이동
        bat.append(2)                # 그 핸드폰은 2% 소모
        ans = 2                      # 새 배터리니까 누적값 2%로 초기화
    idx += 1                         # 모든 과정 끝나면 다음 핸드폰으로 이동
if ans < 100:
    print(ans)
else:
    print(0)