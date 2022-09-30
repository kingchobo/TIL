import sys

T = int(sys.stdin.readline())
for _ in range(T):
    case = sys.stdin.readline().rstrip()
    l = []
    for i in range(len(case)):
        if case[i] == '(':
            l.append(1)
        else:
            if l:
                l.pop(0)
            else:
                print('NO')
                break
    else:
        if l:
            print('NO')
        else:
            print('YES')