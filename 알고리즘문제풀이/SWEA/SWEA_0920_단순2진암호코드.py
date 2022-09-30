# 유효한 암호인지 검사하고, 유효하면 각 자리수의 합을 반환하는 함수
def is_valid(code):
    check = 0
    num = 0
    for i in range(8):
        if i % 2 == 0:
            check += int(code[i]) * 3
            num += int(code[i])
        else:
            check += int(code[i])
            num += int(code[i])

    if check % 10 == 0:
        return num

    return 0


# given info
dct = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
       '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    code = ''

    # [1] 입력을 한 줄씩 받으면서 1이 있으면 그 한 줄만 code에 저장
    for i in range(n):
        temp = input()
        if code:
            pass
        elif '1' in temp:
            code = temp
    # print(code)

    # [2] code를 오른쪽 끝에서 부터 탐색하며 처음 1이 등장하는 위치 찾기
    e = m - 1
    while code[e] == '0':
        e -= 1

    # [3] 시작하는 위치(e-55)에서 부터 7개씩 끊어서 숫자로 변환
    ans = ''
    for i in range(e-55, e, 7):
        ans += str(dct[code[i:i+7]])

    print(f'#{tc}', is_valid(ans))