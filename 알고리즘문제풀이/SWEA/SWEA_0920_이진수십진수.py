def change():
    n = 0
    for i in range(7):
        n += sample[i] * 2 ** i
    ans.insert(0, n)


t = int(input())

for tc in range(1, t+1):
    code = list(map(int, input()))
    ans = []
    while True:
        if len(code) == 0:
            break

        sample = []
        for i in range(7):
            sample.append(code.pop())
        change()

    print(f'#{tc}', *ans)