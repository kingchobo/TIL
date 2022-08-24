import sys
input = sys.stdin.readline

n = int(input())
p_list = list(map(int, input().split()))

p_list.sort()

ans = 0
for i in range(1, n+1):
    ans += sum(p_list[:i])

print(ans)