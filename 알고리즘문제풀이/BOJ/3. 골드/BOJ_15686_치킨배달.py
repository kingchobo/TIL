import sys
from itertools import combinations


def chick_dis(r, c, chickens):
    # 집의 좌표를 받았을 때 해당 집의 치킨거리를 반환하는 함수
    dis = n+n
    for i in chickens:
        if abs(r - i[0]) + abs(c - i[1]) < dis:
            dis = abs(r - i[0]) + abs(c - i[1])
    return dis


n, m = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

houses = []
chickens = []
# 치킨집과 가정집의 좌표를 위의 두 리스트에 저장
for r in range(n):
    for c in range(n):
        if city[r][c] == 1:
            houses.append([r, c])
        elif city[r][c] == 2:
            chickens.append([r, c])

if m == len(chickens):
    # 그냥 안 없애고 바로 도시의 치킨거리 출력
    ans = 0
    for i in houses:
        ans += chick_dis(i[0], i[1], chickens)

else:
    combi = list(combinations(chickens, m))
    ans = 4*n*n
    for i in range(len(combi)):
        temp_ans = 0
        for j in houses:
            temp_ans += chick_dis(j[0], j[1], combi[i])
        if temp_ans < ans:
            ans = temp_ans

print(ans)