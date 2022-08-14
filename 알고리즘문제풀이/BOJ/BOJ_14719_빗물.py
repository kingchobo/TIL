H, W = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

for i in range(1, W-1):
    L = max(arr[:i])
    R = max(arr[i+1:])
    if arr[i] < min(L, R):
        answer += min(L, R) - arr[i]

print(answer)