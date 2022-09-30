def recur(sum_now, i):
    global min_gap

    if i == n:
        gap = sum_now - b
        if gap >= 0:
            if gap < min_gap:
                min_gap = gap
    else:
        recur(sum_now + heights[i], i+1)
        recur(sum_now, i+1)


t = int(input())
for tc in range(1, t+1):
    n, b = map(int, input().split())
    heights = list(map(int, input().split()))
    min_gap = 200001

    recur(0, 0)
    print(f'#{tc} {min_gap}')