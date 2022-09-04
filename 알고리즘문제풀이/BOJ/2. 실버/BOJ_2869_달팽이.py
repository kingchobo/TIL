a, b, v = map(int, input().split())
m = (v - a) // (a - b)
n = (v - a) % (a - b)
if n == 0:
    print(m+1)
else:
    print(m+2)