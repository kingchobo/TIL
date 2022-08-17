T = int(input())
for tc in range(1, T+1):
    n = int(input())
    area = [[0]*n for _ in range(n)]
    for i in range(n):
        area[i][0] = 1
    for j in range(1, n):
        for k in range(1, n):
            area[j][k] = area[j-1][k-1] + area[j-1][k]
    print(f"#{tc}")
    for sub_list in area:
        for num in sub_list:
            if num != 0:
                print(num, end=' ')
            else:
                print()
                break
    print()