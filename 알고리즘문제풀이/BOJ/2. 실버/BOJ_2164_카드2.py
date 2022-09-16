n = int(input())
arr = [i for i in range(1, n+1)]
while True:
    if len(arr) == 1:
        break
    del arr[0]
    if len(arr) == 1:
        break
    arr.append(arr.pop(0))
print(arr[0])