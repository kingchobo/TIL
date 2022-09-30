def postorder(v):
    if v <= n:
        if tree[v] == 0:
            L = postorder(2*v)
            R = postorder(2*v + 1)
            tree[v] = L + R
            return tree[v]
        else:
            return tree[v]
    else:
        return 0

t = int(input())
for tc in range(1, t+1):
    n, m, l = map(int, input().split())
    tree = [0] * (n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a] = b

    postorder(1)

    print(f'#{tc} {tree[l]}')