from sys import stdin

N = int(input())
trees = [tuple(map(int, stdin.readline().split())) for _ in range(N)]


def tree_needed(arr):
    max_x = 0
    min_x = 1000000
    max_y = 0
    min_y = 1000000
    for tree in arr:
        if tree[0] > max_x:
            max_x = tree[0]
        if tree[0] < min_x:
            min_x = tree[0]

        if tree[1] > max_y:
            max_y = tree[1]
        if tree[1] < min_y:
            min_y = tree[1]

    return 2 * ((max_x - min_x) + (max_y - min_y))


def f(subset, i, arr, having):
    global ans
    if i == len(arr):
        if having >= tree_needed(subset):
            ans = min(ans, N - len(subset))
            return

    else:
        subset.append(arr[i])
        i += 1
        f(subset, i, arr, having)
        x = subset.pop()
        f(subset, i, arr, having + x[2])


ans = 40
f([], 0, trees, 0)
print(ans)
