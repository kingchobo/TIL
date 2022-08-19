T = int(input())
for tc in range(T):
    k = int(input())
    n = int(input())
    area = [[1] * n] * (k + 1)
    area[0] = [i for i in range(1, n + 1)]
    for i in range(1, k + 1):
        for j in range(1, n):
            area[i][j] = area[i - 1][j] + area[i][j - 1]
    print(area[-1][-1])