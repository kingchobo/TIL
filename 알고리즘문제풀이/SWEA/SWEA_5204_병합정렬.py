def merge_sort(arr):
    global cnt
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    if left[-1] > right[-1]:
        cnt += 1

    result = []
    i = j = 0
    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i < len(left):
            result.append(left[i])
            i += 1
        elif j < len(right):
            result.append(right[j])
            j += 1

    return result


T = int(input())
for TC in range(1, T+1):
    N = int(input())
    nums_list = list(map(int, input().split()))
    cnt = 0
    ans = merge_sort(nums_list)
    print(f'#{TC} {ans[N//2]} {cnt}')
