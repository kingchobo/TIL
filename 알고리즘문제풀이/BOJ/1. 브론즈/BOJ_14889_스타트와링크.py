# 백준 14889번 문제
'''
자, 예를 들어 4명인 경우를 보자
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

이 상태에서 예를 들어 1,3이 팀이라고 치면
첫 째 줄의 3번째 점수와 셋째 줄의 1번째 점수의 합 - 2째줄의 4번째 항과 4째줄의 2번째 항의 합 의 절대값이 최소인 경우를 찾아야 한다..
개어렵네

'''

N = int(input())
S = []
for i in range(N):
    S.append(list(map(int, input().split())))
# print(S)
# [[0, 1, 2, 3], [4, 0, 5, 6], [7, 1, 0, 2], [3, 4, 5, 0]]
# (S[0][1] + S[1][0]) - (S[2][3] + S[3][2])
dif = []
for i in range(N):
    for j in range(i+1, N):
        enemy = list(range(N))
        enemy.remove(i)
        enemy.remove(j)
        a = (S[i][j] + S[j][i]) - (S[enemy[0]][enemy[1]] + S[enemy[1]][enemy[0]])
        if a < 0:
            a = a * (-1)
        dif.append(a)

print(min(dif))