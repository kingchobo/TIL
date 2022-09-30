T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))

    player_1 = [0] * 10
    run_1 = 0
    triplet_1 = 0

    player_2 = [0] * 10
    run_2 = 0
    triplet_2 = 0

    for i in range(12):
        if i % 2:
            player_2[cards[i]] += 1
        else:
            player_1[cards[i]] += 1

        if i >= 4 and i % 2 == 0:
            for j in range(8):
                if player_1[j] > 0 and player_1[j+1] > 0 and player_1[j+2] > 0:
                    run_1 += 1
                    break
                elif player_1[j] == 3:
                    triplet_1 += 1
                    break

        if i >= 5 and i % 2:
            for j in range(8):
                if player_2[j] > 0 and player_2[j+1] > 0 and player_2[j+2] > 0:
                    run_2 += 1
                    break
                elif player_2[j] == 3:
                    triplet_2 += 1
                    break

        if run_1 + triplet_1 == 1:
            print(f'#{tc} 1')
            break

        if run_2 + triplet_2 == 1:
            print(f'#{tc} 2')
            break

    else:
        print(f'#{tc} 0')