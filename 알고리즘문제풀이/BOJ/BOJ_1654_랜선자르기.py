K, N = map(int, input().split())

# 보유중인 K개의 랜선의 길이 리스트
arr_k = [int(input()) for _ in range(K)]

# 이분탐색의 시작과 끝 위치
start, end = 1, max(arr_k)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in arr_k:
        lines += i // mid

    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)