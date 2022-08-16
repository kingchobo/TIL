arr = list(map(int, input().split()))
test = [1, 2, 3, 4, 5, 6, 7, 8]
if arr == test:
    print('ascending')
elif arr[::-1] == test:
    print('descending')
else:
    print('mixed')