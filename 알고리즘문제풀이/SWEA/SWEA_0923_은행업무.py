def two(num: str):
    result = 0
    x = len(num)
    for y in range(x):
        result += int(num[y]) * 2 ** (x-1-y)
    return result


def three(num: str):
    result = 0
    x = len(num)
    for z in range(x):
        result += int(num[z]) * 3 ** (x-1-z)
    return result


t = int(input())
for tc in range(1, t+1):
    num_2 = input()
    num_3 = input()

    # 가능한 2진수
    possibles_2 = [0] * len(num_2)
    for i in range(len(num_2)):
        if num_2[i] == '1':
            num_2 = num_2[:i] + '0' + num_2[i + 1:]
            possibles_2[i] = two(num_2)
            num_2 = num_2[:i] + '1' + num_2[i + 1:]
        else:
            num_2 = num_2[:i] + '1' + num_2[i + 1:]
            possibles_2[i] = two(num_2)
            num_2 = num_2[:i] + '0' + num_2[i + 1:]

    # 가능한 3진수
    possibles_3 = []
    for i in range(len(num_3)):
        if num_3[i] == '0':
            num_3 = num_3[:i] + '1' + num_3[i + 1:]
            possibles_3.append(three(num_3))
            num_3 = num_3[:i] + '2' + num_3[i + 1:]
            possibles_3.append(three(num_3))
            num_3 = num_3[:i] + '0' + num_3[i + 1:]
        elif num_3[i] == '1':
            num_3 = num_3[:i] + '0' + num_3[i + 1:]
            possibles_3.append(three(num_3))
            num_3 = num_3[:i] + '2' + num_3[i + 1:]
            possibles_3.append(three(num_3))
            num_3 = num_3[:i] + '1' + num_3[i + 1:]
        else:
            num_3 = num_3[:i] + '0' + num_3[i + 1:]
            possibles_3.append(three(num_3))
            num_3 = num_3[:i] + '1' + num_3[i + 1:]
            possibles_3.append(three(num_3))
            num_3 = num_3[:i] + '2' + num_3[i + 1:]

    for i in possibles_2:
        if i in possibles_3:
            print(f'#{tc} {i}')
            break