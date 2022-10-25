import sys
from collections import deque

T = int(input())
for tc in range(T):
    given, target = map(int, sys.stdin.readline().split())
    visited = [0] * 10000
    q = deque()
    q.append((given, ''))
    while q:
        num, ans = q.popleft()
        if num == target:
            print(ans)
            break
        if not visited[num]:
            visited[num] = 1
            q.append(((num * 2) % 10000, ans + 'D'))
            if num == 0:
                q.append((9999, ans + 'S'))
            else:
                q.append((num - 1, ans + 'S'))
            q.append(((num % 1000) * 10 + (num // 1000), ans + 'L'))
            q.append(((num // 10) + 1000 * (num % 10), ans + 'R'))