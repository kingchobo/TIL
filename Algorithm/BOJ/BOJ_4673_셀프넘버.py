# 백준 4673번 문제
def is_self_num():
    '''1부터 10000까지 숫자들로 생성자들을 만들어서 not_self_num리스트에 담아두고,
    해당 리스트에 들어있지 않은 숫자들은 생성자가 없는 것이므로 self number.
    '''
    not_self_num = []
    for num in range(10001):
        if num + sum_seperated_num(num) <= 10000:
            not_self_num.append(num + sum_seperated_num(num))
    for num in range(10001):
        if num not in not_self_num:
            print(num)
    
def sum_seperated_num(num):
    # 숫자의 각 자리수의 합 구하는 함수
    if num < 10:
        return num
    else:
        return sum_seperated_num(num//10) + num%10

is_self_num()