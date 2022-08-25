import sys

input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    if n == 0:
        print(0)
        continue

    clothes = {}
    for _ in range(n):
        a, b = input().split()
        if b in clothes.keys():
            clothes[b] += 1
        else:
            clothes[b] = 1

    mul = 1
    for i in clothes.keys():
        mul *= (clothes[i] + 1)

    print(mul - 1)