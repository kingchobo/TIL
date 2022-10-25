def f(day, result):
    global ans
    if result > ans:
        ans = result

    for d in range(day, n):
        if d + time[d] <= n:
            f(d + time[d], result + price[d])


n = int(input())
time = [0] * n
price = [0] * n
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    time[i] = a
    price[i] = b

f(0, 0)
print(ans)