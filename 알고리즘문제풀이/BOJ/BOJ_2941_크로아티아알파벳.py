word = input()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for i in cro:
    if i == 'dz=':
        cnt += 2 * word.count(i)
    else:
        cnt += 1 * word.count(i)
if 'dz=' in word and 'z=' in word:
    cnt -= word.count('dz=')

print(len(word) - cnt)