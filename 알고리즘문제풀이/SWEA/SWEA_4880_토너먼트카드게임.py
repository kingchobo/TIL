def rps(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        if arr[0][1] == arr[1][1]:
            if arr[0][0] < arr[1][0]:
                return arr[0]
            else:
                return arr[1]
        elif arr[0][1] == 1 and arr[1][1] == 2:
            return arr[1]
        elif arr[0][1] == 1 and arr[1][1] == 3:
            return arr[0]
        elif arr[0][1] == 2 and arr[1][1] == 1:
            return arr[0]
        elif arr[0][1] == 2 and arr[1][1] == 3:
            return arr[1]
        elif arr[0][1] == 3 and arr[1][1] == 1:
            return arr[1]
        elif arr[0][1] == 3 and arr[1][1] == 2:
            return arr[0]

    else:
        if len(arr) % 2:
            return rps([rps(arr[:len(arr)//2 + 1]), rps(arr[len(arr)//2 + 1:])])
        else:
            return rps([rps(arr[:len(arr)//2]), rps(arr[len(arr)//2:])])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rps_list = list(map(int, input().split()))
    num_list = [i for i in range(1, N+1)]
    new_list = []
    for i in range(N):
        new_list.append((num_list[i], rps_list[i]))

    print(f'#{tc} {rps(new_list)[0]}')