def sum_seperated_num(num):
    # 숫자의 각 자리수의 합 구하는 함수
    if num < 10:
        return num
    else:
        return sum_seperated_num(num // 10) + num % 10