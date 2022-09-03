n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
cnt = 0
# 종료 조건
while True:
    m = max(arr)
    if arr[0] == m and arr.count(m) == 1:
        break
    elif arr[0] == m and arr.count(m) >= 2:
        cnt += 1
        break
    else:
        arr[arr.index(m)] -= 1
        arr[0] += 1
        cnt += 1
print(cnt)