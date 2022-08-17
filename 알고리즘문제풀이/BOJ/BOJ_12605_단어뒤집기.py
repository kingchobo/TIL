T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    for i in range(len(arr)//2):
        arr[i], arr[-1-i] = arr[-1-i], arr[i]
    print(f"Case #{tc}: ", end='')
    print(' '.join(arr))