N = int(input())
mul = 1

for i in range(1, N+1):
    mul *= i

cnt = 0
while True:
    if mul % 10 == 0:
        mul //= 10
        cnt += 1
    else:
        break

print(cnt)