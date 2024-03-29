def binary_search(b, l, r, d):
    global cnt
    m = (l+r) // 2
    if A[m] == b:
        cnt += 1
        return

    if l > r:
        return

    elif A[l] <= b < A[m]:
        if d == 1:
            return
        else:
            binary_search(b, l, m-1, 1)

    elif A[m] < b <= A[r]:
        if d == 2:
            return
        else:
            binary_search(b, m+1, r, 2)


T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for num in B:
        binary_search(num, 0, N-1, 0)
    print(f'#{TC} {cnt}')