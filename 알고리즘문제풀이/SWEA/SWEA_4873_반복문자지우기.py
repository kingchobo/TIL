def del_words(arr):
    i = 0
    new_arr = []
    while True:
        if i == len(arr) - 1:
            new_arr.append(arr[i])
            break
        if i == len(arr):
            break
        if arr[i] != arr[i+1]:
            new_arr.append(arr[i])
            i += 1
        else:
            i += 2
    return new_arr

T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    ans = arr[:]
    for i in range(len(arr)//2):
        ans = del_words(ans)
    print(f'#{tc} {len(ans)}')