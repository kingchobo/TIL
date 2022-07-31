# 백준 4344번 문제
import statistics
C = int(input())

for case in range(C):
    scores = list(map(int, input().split()))
    N = list[0]
    scores_list = scores[1:]
    average = statistics.mean(scores_list)
    over_avg = []
    for score in scores_list:
        if score > average:
            over_avg.append(score)
    print(f'{len(over_avg) * 100 / len(scores_list):.3f}%')