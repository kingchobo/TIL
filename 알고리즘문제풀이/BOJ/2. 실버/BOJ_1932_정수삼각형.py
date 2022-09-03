n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

if n == 1:
    print(triangle[-1][0])

else:
    triangle[1][0] += triangle[0][0]
    triangle[1][1] += triangle[0][0]

    for i in range(2, n):
        for j in range(len(triangle[i])):
            if j == 0: # 왼쪽 끝 값일 때
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1: # 오른쪽 끝 값일 때
                triangle[i][j] += triangle[i - 1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    print(max(triangle[-1]))