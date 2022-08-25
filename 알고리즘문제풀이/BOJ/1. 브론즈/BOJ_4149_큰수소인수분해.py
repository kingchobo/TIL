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
    for i in range(2, int(num**0.5)+1):
        if prime_number(i):
            prime_num_list.append(i)
    i = 0
    factorized_list = []
    L = len(prime_num_list)
    while i < L:
        if num % prime_num_list[i] == 0:
            factorized_list.append(prime_num_list[i])
            num //= prime_num_list[i]
        else:
            i += 1
    if len(factorized_list) == 0:
        factorized_list.append((num))

    return factorized_list

n = int(input())
for i in factorization(n):
    print(i)
