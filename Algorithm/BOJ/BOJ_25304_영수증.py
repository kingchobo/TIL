X = int(input())
N = int(input())
price_list = []
for i in range(N):
    price_quan = tuple(map(int, input().split()))
    price_list.append(price_quan)
# price_list = [(20000, 5), (30000, 2), (10000, 6), (5000, 8)]

sum = 0
for i in price_list:
    sum += i[0] * i[1]

if sum == X:
    print('Yes')
else:
    print('No')