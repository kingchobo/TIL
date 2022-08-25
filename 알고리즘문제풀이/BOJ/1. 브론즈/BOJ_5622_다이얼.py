word = input()
words = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
nums = [2,3,4,5,6,7,8,9]
answer1 = []
for i in word:
    for j in words:
        if i in j:
            a = words.index(j)
            answer1.append(nums[a])
time = 0
for k in answer1:
    time += 2 + (k-1)

print(time)