n, m = map(int, input().split())
mul1 = mul2 = 1
for i in range(m):
    mul1 *= (n-i)
    mul2 *= (m-i)
print(mul1//mul2)