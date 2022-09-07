import sys
k = int(sys.stdin.readline())
height = 0
width = 0
arr = []
empty_area = 1
for _ in range(6):
    direction, length = map(int, sys.stdin.readline().split())
    arr.append((direction, length))
    if direction == 1:
        width += length
    elif direction == 3:
        height += length

if arr[0][0] == 1 or arr[0][0] == 2:
    if arr[0][1] < width:
        empty_area = arr[1][1] * arr[2][1]
    elif arr[0][1] == width:
        if arr[1][1] < height:
            empty_area = arr[2][1] * arr[3][1]
        elif arr[1][1] == height:
            empty_area = arr[3][1] * arr[4][1]

elif arr[0][0] == 3 or arr[0][0] == 4:
    if arr[0][1] < height:
        empty_area = arr[1][1] * arr[2][1]
    elif arr[0][1] == height:
        if arr[1][1] < width:
            empty_area = arr[2][1] * arr[3][1]
        elif arr[1][1] == width:
            empty_area = arr[3][1] * arr[4][1]

total_area = width * height
print(k * (total_area - empty_area))
