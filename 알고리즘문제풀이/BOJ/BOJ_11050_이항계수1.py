n, k = map(int, input().split())

if n-k < k:
    k = n-k

up = 1
down = 1
for i in range(k):
    up *= n
    n -= 1
    down *= k
    k -= 1

print(up//down)