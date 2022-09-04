import sys
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

def prime_number(n):
    # 소수 판별 함수
    if n <= 1:
        return False
    elif n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

cnt = 0
for i in num_list:
    if prime_number(i):
        cnt += 1
print(cnt)