import sys

n = int(sys.stdin.readline())
arr = [0] * n
for i in range(n):
    arr[i] = int(sys.stdin.readline())

if n == 1:
    print(0)

else:
    cnt = 0
    while len(arr) > 1:
        temp = arr.pop(arr.index(min(arr))) + arr.pop(arr.index(min(arr)))
        cnt += temp
        arr.append(temp)

# else:
#     arr.sort()
#     temp_1 = []
#     temp_2 = []
#     cnt = 0
#     while len(arr) > 0:
#         if not temp_1:
#             temp_2.append(arr.pop(0))
#         else:
#             if arr[0] < temp_1[0]:
#                 temp_2.append(arr.pop(0))
#             else:
#                 temp_2.append(temp_1.pop(0))
#
#         if len(temp_2) == 2:
#             cnt += sum(temp_2)
#             temp_1.append(sum(temp_2))
#             temp_2 = []
#
#     if len(temp_2) == 0:
#         if len(temp_1) == 1:
#             print(cnt)
#         else:
#             while len(temp_1) > 0:
#
#
#     ㅈㅈ
#
#
#     if len(temp_1) + len(temp_2) == 1:
#         print(cnt)
#     else:
#         print(cnt + sum(temp_1) + sum(temp_2))