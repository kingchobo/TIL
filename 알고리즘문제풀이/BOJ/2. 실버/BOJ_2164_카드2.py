n = int(input())

if n == 1:
    print(1)

else:
    i = 1
    while 2**i <= n:
        i += 1
    if 2**(i-1) == n:
        print(n)
    else:
        print((n - 2**(i-1)) * 2)

