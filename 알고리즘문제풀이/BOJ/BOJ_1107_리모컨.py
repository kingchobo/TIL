n = int(input())
m = int(input())
if m == 0:
    print(len(str(n)))
else:
    arr = list(map(int, input().split()))
    cnt = 0
    # 고장 안난 버튼 모음
    arr_new = []
    for i in range(0, 10):
        if i not in arr:
            arr_new.append(i)

    # 특정 채널의 경우 분리
    if n == 100:
        print(0)
    elif n == 99 or n == 101:
        print(1)
    elif n == 102:
        print(2)

    # 리모컨의 상태에 따른 분리
    elif m == 10:
        if n > 100:
            print(n - 100)
        else:
            print(100 - n)

    # 나머지 경우
    else:
        m_l = []
        i_l = []
        s = str(n)
        l = len(s)
        channel = ''
        for _ in range(len(s)):
            a = int(s[_])
            # 만약 a가 고장난 버튼이면,
            if a in arr:    # n의 첫 자리 수와 절대값의 차이가 가장 작은 고장 안난 버튼 찾기 = b
                for i in arr_new:
                    m = i - a
                    if m < 0:
                        m *= (-1)
                    m_l.append(m)
                    i_l.append(i)
                m = min(m_l)
                b = i_l[m_l.index(m)]
                if b < a:
                    channel += str(b) + str(max(arr_new)) * (l-1)
                    cnt += l
                    break
                else:
                    channel += str(b) + str(min(arr_new)) * (l-1)
                    cnt += l
                    break
            else:
                cnt += 1
                l -= 1
                channel += str(a)

        compare1 = 100 - n    # 순수 +, - 노가다
        if compare1 < 0:
            compare1 *= -1

        compare2 = 500001
        if 1 in arr_new and n < 100000:
            compare2 = int('1' * (len(str(n))+1)) - n + (len(str(n))+1)

        compare3 = 500001
        if 1 in arr_new and 0 in arr_new and n < 100000:
            compare3 = int('1' + '0'*(len(str(n)))) - n + (len(str(n))+1)

        compare4 = 500001
        if n >= 10:
            compare4 = n - int(str(max(arr_new)) * (len(str(n))-1)) + (len(str(n))-1)

        compare5 = 500001
        if n < 100000:
            compare22 = int(str(min(arr_new)) * (len(str(n)) + 1)) - n + (len(str(n)) + 1)

        compare6 = 500001
        if int(str(n)[0])-1 in arr_new:
            compare6 = n - int(str(int(str(n)[0])-1) + str(max(arr_new)) * (len(str(n))-1)) + len(str(n))

        if n - int(channel) < 0:
            cnt += (n - int(channel)) * (-1)
            print(min(cnt, compare1, compare2, compare3, compare4, compare5, compare6))
        else:
            cnt += (n - int(channel))
            print(min(cnt, compare1, compare2, compare3, compare4, compare5, compare6))