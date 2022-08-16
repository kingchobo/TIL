T = int(input())
for tc in range(1, T+1):
    A, B = input().split()    # banana bana
    N = len(A)     # 6
    M = len(B)     # 4
    cnt = 0
    i = 0
    # A에서 길이 M만큼 슬라이싱 하며 B과 같아지는지 탐색
    while True:
        if i > N-M+1:
            break
        elif A[i:i+M] == B:
            cnt += 1
            i += M
        else:
            i += 1

    print(f"#{tc} {N - cnt*M + cnt}")