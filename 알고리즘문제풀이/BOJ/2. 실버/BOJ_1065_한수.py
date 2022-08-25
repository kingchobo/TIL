# 백준 1065번 문제
n = int(input())

def solve(n):
    '''
    n < 100의 경우에는 return n
    1000> n > 100의 경우에는 99 + 100이상에서의 등차수열의 개수
    n == 1000의 경우는 위와 개수는 같지만 식이 달라질 수 있으므로 따로 빼자.
    100~999에서의 등차수열의 경우는
    1) 세자리 수가 다 같을 때(def == 0) : 111, 222, 333 등
    2) 공차가 양수일 때 : 123, 258 등
    3) 공차가 음수일 때 : 321, 963 등
    '''
    cnt = 0
    if n < 100:
        return n
    elif 100 <= n < 1000:
        for num in range(100, n+1):
            listed_num = list(map(int, (str(num))))
            # ex. listed_num = [1, 2, 3]
            if listed_num[0] < listed_num[-1]:
                dif = listed_num[-1] - listed_num[0]
                dif = int(dif / 2)
                new_list = [listed_num[0]]
                for i in range(2):
                    new_list.append(new_list[-1] + dif)
                    if new_list == listed_num:
                        cnt += 1
            elif listed_num[0] == listed_num[-1] == listed_num[1]:
                cnt += 1
            else:
                # ex. 531
                dif = listed_num[0] - listed_num[-1]
                dif = int(dif / 2)
                new_list = [listed_num[0]]
                for i in range(2):
                    new_list.append(new_list[-1] - dif)
                    if new_list == listed_num:
                        cnt += 1
        return 99 + cnt
    else:
        return solve(n-1)

print(solve(n))