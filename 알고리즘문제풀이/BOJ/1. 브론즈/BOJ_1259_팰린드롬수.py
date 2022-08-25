def is_palindrome(num):
    check = str(num)
    for i in range(len(check)//2):
        if check[i] != check[-1-i]:
            return 0
    else:
        return 1

while True:
    n = int(input())
    if n == 0:
        break
    print('yes') if is_palindrome(n) else print('no')