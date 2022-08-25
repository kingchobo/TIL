T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:
        YY = H * 100
        XX = N // H

    else:
        YY = N % H * 100
        XX = N // H + 1
    print(YY+XX)