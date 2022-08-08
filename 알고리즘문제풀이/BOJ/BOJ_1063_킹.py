# 백준 1063번 문제
'''
첫째 줄에 킹의위치(A1), 돌의위치(A2), 움직이는 횟수 N 입력

출력 : 첫째 줄에 킹의 마지막 위치, 둘째 줄에 돌의 마지막 위치
'''
king, stone, N = input().split()
k = [ord(king[0]), int(king[1])]
s = [ord(stone[0]), int(stone[1])]

for i in range(int(N)):
    move = input()
    if move == 'R':
        king[1] += 1
    elif move == 'L':
        king[1] -= 1
    