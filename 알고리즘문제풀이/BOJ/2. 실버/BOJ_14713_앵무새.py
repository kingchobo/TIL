import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [list(input().split()) for _ in range(N)]
test = list(input().split())

cnt = 0
for i in range(len(test)):
    for j in arr:
        if j and test[i] == j[0]:
            del j[0]
            cnt += 1
            break
    else:
        break

cnt2 = 0
for i in arr:
    cnt2 += len(i)

if cnt == len(test) and cnt2 == 0:
    print('Possible')
else:
    print('Impossible')