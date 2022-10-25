N, M = map(int, input().split())

area = [i for i in range(101)]
visited = [0] * 101
for i in range(N+M):
    s, e = map(int, input().split())
    area[s] = e

q = [(1, 0)]        # (현재 위치, 지금까지 이동한 횟수)
ans = 0

while q:
    cur, times = q.pop(0)
    if cur == 100:
        ans = times
        break

    else:
        for i in range(1, 7):
            temp_cur = cur + i
            if 1 <= temp_cur <= 100 and not visited[temp_cur]:
                visited[temp_cur] = 1
                q.append((area[temp_cur], times + 1))

print(ans)