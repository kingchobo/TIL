K, N = map(int, input().split())
l = []
for i in range(K):
    l.append(int(input()))
# l = [802, 743, 457, 539]
best = sum(l) // N
# best = 231
new_l = []
for i in l:
    new_l.append(i//best)
# new_l = [3, 3, 1, 2]
n = sum(new_l)
# n = 9
if n == N:
    print(best)
else:
    while n < N:
        m = 0
        c = 0
        for i in range(K):    # 남은 길이가 가장 긴 랜선의 인덱스 찾기
            if m < l[i] - best * new_l[i]:
                m = l[i] - best * new_l[i]
                c = i
        # 그 랜선의 개수(new_l[c])가 +1 이 되도록 best를 줄임
        best = l[c] // (new_l[c] + 1)
        new_l.clear()
        for i in l:
            new_l.append(i//best)
        n = sum(new_l)
        if n >= N:
            print(best)