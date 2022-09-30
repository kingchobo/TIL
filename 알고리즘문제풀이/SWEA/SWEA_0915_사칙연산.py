def postorder(v):
    if v <= n:
        if len(son[v]):
            L = postorder(son[v][0])
            R = postorder(son[v][1])
            if tree[v] == '+':
                tree[v] = L + R
            elif tree[v] == '-':
                tree[v] = L - R
            elif tree[v] == '*':
                tree[v] = L * R
            elif tree[v] == '/':
                tree[v] = L / R
            return tree[v]

        else:
            return tree[v]


t = 10
for tc in range(1, t+1):
    n = int(input())
    tree = [0] * (n+1)
    son = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        arr = list(input().split())
        if len(arr) == 4:
            tree[i] = arr[1]
            son[i] = [int(arr[2]), int(arr[3])]
        else:
            tree[i] = int(arr[1])

    print(f'#{tc} {int(postorder(1))}')