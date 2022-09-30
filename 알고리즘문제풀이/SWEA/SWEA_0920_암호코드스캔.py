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


# 16진수의 2진수 변환 딕셔너리
dct = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
       '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())

    # [1] 한 줄씩 입력 받으면서, 0이 아닌 문자가 들어있으면 case에 추가. 이미 case에 있으면 추가 x
    case_list = []
    for i in range(n):
        temp = input()
        for j in temp:
            if j != '0':
                if temp not in case_list:
                    case_list.append(temp)
                break

    # [2] case_list 내의 각 case에 대하여 2진수로 변환
    for case in case_list:
        code = ''
        for ch in case:
            code += dct[ch]

        # [3] code의 우측 끝에서 부터 1이 처음 등장하는 인덱스 찾기
        e = len(code) - 1
        while code[e] == '0':
            e -= 1

        # [4] e 위치에서 부터 역순으로 이동하며 비율 찾기
        ratio = [0] * 4
        cnt = 0
        while True:
            if code[e] == code[e-1]:


    # # [2] case 리스트 내의 각 case에 대하여 뒤에서 부터 0이 아닌 자리를 탐색
    # # [2-1] 처음부터 그 자리(e)까지 2진수로 변환
    # for case in case_list:
    #     e = m - 1
    #     while case[e] == '0':
    #         e -= 1
    #     for i in range(e):
    #