def binary(s, e):
    while s <= e:
        mid = (s+e) // 2
        if mid**3 == n:
            return mid
        elif mid**3 < n:
            s = mid + 1
        else:
            e = mid - 1
    return -1

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    end = int(n ** (1/2))
    print(f'#{tc} {binary(1, end)}')