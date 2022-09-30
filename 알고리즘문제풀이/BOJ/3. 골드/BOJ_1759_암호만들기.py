import itertools

L, C = map(int, input().split())
lst = list(input().split())
lst.sort()
vowels = ['a', 'e', 'i', 'o', 'u']
comb = itertools.combinations(lst, L)
for i in comb:
    st = ''
    num_vowels = 0
    num_consonants = 0
    for ch in i:
        st += ch
        if ch in vowels:
            num_vowels += 1
        else:
            num_consonants += 1
    if num_consonants >= 2 and num_vowels >= 1:
        print(st)