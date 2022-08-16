T = int(input())

for tc in range(1, T+1):
    arr = list(input())
    ans = 0
    cnt = 0
    for i in range(len(arr)-1):
        if arr[i] == '(' and arr[i+1] == ')':
            ans += cnt
        elif arr[i] == '(':
            ans += 1
            cnt += 1
        elif arr[i] == ')' and arr[i-1] != '(':
            cnt -= 1
    print(f'#{tc} {ans}')