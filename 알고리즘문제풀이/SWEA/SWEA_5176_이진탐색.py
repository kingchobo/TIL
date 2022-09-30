def inorder(v):
    if v <= n:
        inorder(v*2)
        tree[v] = num_list.pop(0)
        inorder(v*2 + 1)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    num_list = [i for i in range(1,n+1)]
    tree = [0] * (n+1)
    inorder(1)

    print(f'#{tc} {tree[1]} {tree[n//2]}')