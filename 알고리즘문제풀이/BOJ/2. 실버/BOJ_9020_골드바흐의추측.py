def prime_number(n):
    # 소수 판별 함수
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    n = int(input())
    a, b = n//2, n//2
    for i in range(n//2):
        if prime_number(a) and prime_number(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1