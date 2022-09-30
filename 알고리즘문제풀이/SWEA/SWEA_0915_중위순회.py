def inorder(v):
    global answer
    if v <= N:
        inorder(v*2)      # 좌
        answer += tree[v]
        inorder(v*2 + 1)  # 우


T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    for _ in range(N):
        a, b, *c = input().split()
        tree[int(a)] = b

    answer = ''
    inorder(1)
    print(f'#{tc} {answer}')