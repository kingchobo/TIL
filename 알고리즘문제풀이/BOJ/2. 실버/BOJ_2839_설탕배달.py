N = int(input())
if N < 5:
    if N == 3:
        print(1)
    else:
        print(-1)
else:
    a, b = N // 5, N % 5
    if b == 0:
        print(a)
    elif b == 3:
        print(a + 1)
    else:
        while a > 0:
            a -= 1
            b += 5
            if b % 3 == 0:
                print(a + b//3)
                break
        else:
            print(-1)