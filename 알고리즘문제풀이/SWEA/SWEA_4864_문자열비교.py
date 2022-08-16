T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)

    # str2에서 길이 N만큼 슬라이싱 하며 str1과 같아지는지 탐색
    for i in range(M-N+1):
        if str2[i:i+N] == str1:
            print(f"#{tc} 1")
            break
    else:
        print(f"#{tc} 0")