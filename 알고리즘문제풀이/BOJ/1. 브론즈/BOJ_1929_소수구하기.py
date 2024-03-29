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

M, N = map(int, input().split())
for i in range(M, N+1):
    if prime_number(i):
        print(i)