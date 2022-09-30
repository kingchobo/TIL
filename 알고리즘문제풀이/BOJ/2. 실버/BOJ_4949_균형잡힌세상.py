import sys

open_bracket_list = ['(', '{', '[']
close_bracket_list = [')', '}', ']']

while True:
    case = list(sys.stdin.readline().rstrip())
    if len(case) == 1:
        break
    temp = []
    for i in case:
        if i in open_bracket_list:
            temp.append(i)
        elif i in close_bracket_list:
            if temp:
                last = temp.pop()
                if last != open_bracket_list[close_bracket_list.index(i)]:
                    print('no')
                    break
            else:
                print('no')
                break
    else:
        if temp:
            print('no')
        else:
            print('yes')