t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    tree = [0] * (n+1)
    for i in range(1, n+1):
        tree[i] = arr[i]
        if tree[i//2] > tree[i]:
            while tree[i//2] > tree[i]:
                tree[i], tree[i//2] = tree[i//2], tree[i]
                i //= 2

    josang_sum = 0
    while True:
        josang_sum += tree[n//2]
        n //= 2
        if n == 0:
            break

    print(f'#{tc} {josang_sum}')