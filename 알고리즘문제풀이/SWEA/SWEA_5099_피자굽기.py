t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    cheeses = list(map(int, input().split()))

    # pizza list에 피자의 번호와 치즈의 양을 tuple로 저장
    pizza = []
    for i in range(m):
        pizza.append((i+1, cheeses[i]))

    # fire(화덕) list에 화덕의 개수(n) 만큼 피자를 넣음
    fire = []
    for i in range(n):
        fire.append(pizza.pop(0))

    # 화덕에 피자가 하나 남을 때 까지 반복
    # 화덕에서 피자를 꺼내봄과 동시에 cheese //= 2를 해주고,
    # 그 값이 0이 아니면 다시 넣고,
    # 0이면서 더 넣을 피자가 피자리스트에 남아있다면 넣음
    # 0이면서 더 넣을 피자가 피자리스트에 남아있지 않다면 첫 줄의 pop(0)에 의해
    # 화덕의 남은 피자 개수가 1이 될때까지 계속 꺼내짐
    while len(fire) != 1:
        num, cheese = fire.pop(0)
        cheese //= 2
        if cheese != 0:
            fire.append((num, cheese))

        elif pizza:
            fire.append(pizza.pop(0))

    print(f'#{tc} {fire[0][0]}')