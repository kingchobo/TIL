T = int(input())
for TC in range(1, T+1):
    N = int(input())
    bus_list = []
    for _ in range(N):
        a, b = map(int, input().split())
        bus_list.append((a, b))
    P = int(input())
    C_list = []
    for _ in range(P):
        C_list.append(int(input()))

    ans = [0] * P
    for i in range(P):
        for j in bus_list:
            if C_list[i] in range(j[0], j[1]+1):
                ans[i] += 1
    print(f'#{TC}', *ans)