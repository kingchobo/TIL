def binary_search(s, e, result):
    mid = (s+e) // 2
    if s > e:
        return mid

    for tree in heights:
        if tree - mid > 0:
            result += (tree - mid)
    if result == M:
        return mid

    if result > M:
        return binary_search(mid+1, e, 0)

    else:
        return binary_search(s, mid-1, 0)


N, M = map(int, input().split())
heights = list(map(int, input().split()))

s = 0
e = max(heights)

result = 0
ans = binary_search(s, e, 0)

print(ans)