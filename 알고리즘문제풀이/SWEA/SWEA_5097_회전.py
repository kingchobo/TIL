t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{tc} {arr[m % n]}')