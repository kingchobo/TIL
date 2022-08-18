N = int(input())

i = 1
cnt = 2
if N == 1:
    cnt = 1
elif N < 8:
    cnt = 2
else:
    while N-1 > 6*i:
        N -= 6*i
        i += 1
        cnt += 1
print(cnt)