N = int(input())
# 0 3 5 6 8 9 12 13 14 15 17 18 19 21 24 27 ...
if N % 5 == 0:
    print(N//5)
else:
    for i in range(1, N//5 + 1, -1):
        if (N//i) % 3 == 0:
            print(N//i + N%i)
if (N % 5) % 3 == 0:

if N % 3 == 0:
    