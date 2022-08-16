T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    my_dict = {key: 0 for key in str1}
    for char in str2:
        if char in my_dict:
            my_dict[char] += 1

    max_value = 0
    for i in my_dict.values():
        if i > max_value:
            max_value = i
    answer = [k for k,v in my_dict.items() if v == max_value]

    print(f'#{tc} {my_dict[answer[0]]}')