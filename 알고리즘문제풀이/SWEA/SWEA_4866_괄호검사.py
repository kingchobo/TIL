T = int(input())
for tc in range(1, T+1):
    text = input()
    opener = ['(','{','[']
    closer = [')', '}', ']']
    check = []
    ans = 1
    for i in text:
        if i in opener:
            check.append(i)
        if i in closer:
            if len(check) == 0:
                ans = 0
                break
            if closer.index(i) == opener.index(check[-1]):
                check.pop()
            else:
                ans = 0
                break
    if len(check) != 0:
        ans = 0

    print(f'#{tc} {ans}')