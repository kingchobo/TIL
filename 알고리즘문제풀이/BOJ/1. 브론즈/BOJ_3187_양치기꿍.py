R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

for i in range(R):
    if 'v' in arr[i]:
        v = arr[i].find('v')
        break
else:
