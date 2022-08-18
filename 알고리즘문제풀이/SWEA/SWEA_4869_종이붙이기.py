def paper_10(n, cnt):
    # 10을 우선으로 넣는 스택
    if n < 10:
        cnt += 1
        return cnt
    elif n < 20:
        cnt += 1
        return cnt
    else:
        return paper_10(n-10, cnt) + 2 * paper_20(n-20, cnt)

def paper_20(n, cnt):
    # 20을 우선으로 넣는 스택
    if n < 20:
        cnt += 1
        return cnt
    else:
        return paper_10(n-10, cnt) + 2 * paper_20(n-20, cnt)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # 인자로 넘길 초기 cnt값 0 선언
    cnt = 0
    if n == 10:
        cnt = 1
    else:
        cnt = paper_10(n-10, cnt) + 2 * paper_20(n-20, cnt)
    print(f'#{tc} {cnt}')