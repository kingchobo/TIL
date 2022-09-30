input_list = [1,2,3,4,5]
used = [0] * len(input_list)
result = []

def perm(arr, n):
    if n == len(input_list):
        result.append(arr[:])
        return
    else:
        for i in range(len(input_list)):
            if not used[i]:
                used[i] = 1
                arr.append(input_list[i])
                perm(arr, n+1)
                arr.pop()
                used[i] = 0

perm([], 0)
print(result)