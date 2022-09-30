import sys
area = [list(sys.stdin.readline().split()) for _ in range(5)]

xi = [0, 0, 1, -1]
yj = [1, -1, 0, 0]
case_list = []

# 롤러코스터 로직 설명
# 델타 4방향 계속 돌리면서 매번 현재 문자열에 해당 글자 하나씩 추가
# 그렇게 5번 하면 6글자되는데 그게 case_list에 없으면 추가
for i in range(5):
    for j in range(5):
        temp = area[i][j]   # 우선 시작위치 글자(숫자) 저장
        for a in range(4):  # 1번
            ai, aj = i + xi[a], j + yj[a]
            if 0 <= ai <= 4 and 0 <= aj <= 4:
                temp_a = temp + area[ai][aj]  # 글자 이어붙이기. 이하 동일
                for b in range(4):  # 2번
                    bi, bj = ai + xi[b], aj + yj[b]
                    if 0 <= bi <= 4 and 0 <= bj <= 4:
                        temp_b = temp_a + area[bi][bj]
                        for c in range(4):  # 3번
                            ci, cj = bi + xi[c], bj + yj[c]
                            if 0 <= ci <= 4 and 0 <= cj <= 4:
                                temp_c = temp_b + area[ci][cj]
                                for d in range(4):  # 4번
                                    di, dj = ci + xi[d], cj + yj[d]
                                    if 0 <= di <= 4 and 0 <= dj <= 4:
                                        temp_d = temp_c + area[di][dj]
                                        for e in range(4):  # 5번
                                            ei, ej = di + xi[e], dj + yj[e]
                                            if 0 <= ei <= 4 and 0 <= ej <= 4:
                                                temp_e = temp_d + area[ei][ej]
                                                if temp_e not in case_list:
                                                    case_list.append(temp_e)

print(len(case_list))