arr = [1,2,3,4,5]
result = []
subset = []


def make_subset(i):
    if i == len(arr):
        result.append(subset[:])
        return
    else:
        subset.append(arr[i])
        i += 1
        make_subset(i)
        subset.pop()
        make_subset(i)


make_subset(0)
print(*result)