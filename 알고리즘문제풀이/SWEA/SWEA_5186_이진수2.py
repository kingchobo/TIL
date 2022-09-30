t = int(input())

for tc in range(1, t+1):
    n = float(input())
    ans = ''
    for i in range(1, 13):
        if n >= 1 / 2**i:
            n -= 1 / 2**i
            ans += '1'

        elif n < 1 / 2**i:
            ans += '0'

        if n == 0:
            print(f'#{tc} {ans}')
            break

    else:
        print(f'#{tc} overflow')