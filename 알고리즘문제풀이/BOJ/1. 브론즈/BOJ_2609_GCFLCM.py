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

def factorization(num):
    # 소인수분해
    # num보다 같거나 작은 소수들을 찾은 뒤, 그 소수들로 나누면서 나눠지는 소수들을 리스트에 담아서 반환
    prime_num_list = []
    for i in range(2, num+1):
        if prime_number(i):
            prime_num_list.append(i)
    idx = 0
    factorized_list = []
    L = len(prime_num_list)
    while idx < L:
        if num % prime_num_list[idx] == 0:
            factorized_list.append(prime_num_list[idx])
            num //= prime_num_list[idx]
        else:
            idx += 1
    if len(factorized_list) == 0:
        factorized_list.append((num))
    return factorized_list

a, b = map(int, input().split())
A = factorization(a)
B = factorization(b)

GCF = 1
LCM = 1
# 최대공약수 찾기
for i in A:
    if i in B:
        GCF *= i
        B.remove(i)
# 최소공배수 찾기
for i in (A + B):
    LCM *= i
print(GCF)
print(LCM)