t = int(input())
for tc in range(1, t+1):
    card_list = list(map(int, input()))
    cnt_list = [0] * 10
    learn = 0
    triplet = 0
    for i in card_list:
        cnt_list[i] += 1
    for i in range(8):
        if cnt_list[i] > 0 and cnt_list[i+1] > 0 and cnt_list[i+2] > 0:
            if cnt_list[i] == 2 and cnt_list[i+1] == 2 and cnt_list[i+2] == 2:
                learn += 2
                break
            else:
                learn += 1
                cnt_list[i] -= 1
                cnt_list[i+1] -= 1
                cnt_list[i+2] -= 1
        if cnt_list[i] >= 3:
            if cnt_list[i] == 6:
                triplet += 2
                break
            else:
                triplet += 1
                cnt_list[i] -= 3
    if learn + triplet == 2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')