import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())

    if n == 0:
        print(0)
        continue

    clothes = []
    for _ in range(n):
        a, b = input().split()
        clothes.append((a, b))
    # [('hat', 'headgear'), ('sunglasses', 'eyewear'), ('turban', 'headgear')]

    ans = {}
    for i in clothes:
        ans[i[1]] = []

    for i in ans:
        for j in clothes:
            if i in j:
                ans[i].append(j[0])
    # {'headgear': ['hat', 'turban'], 'eyewear': ['sunglasses']}
    a = 1
    for i in ans:
        a *= (len(ans[i]) + 1)

    print(a-1)