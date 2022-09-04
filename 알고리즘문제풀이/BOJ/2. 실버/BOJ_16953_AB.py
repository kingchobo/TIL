a, b = map(int, input().split())
cnt = 1
ans = True
# 함수
while a < b:
    if b % 10 == 1:
        b = (b-1) // 10
        cnt += 1
    elif b % 2 == 0:
        b //= 2
        cnt += 1
    else:
        ans = False
        break

# 출력
if not ans:
    print(-1)
elif a == b:
    print(cnt)
else:
    print(-1)