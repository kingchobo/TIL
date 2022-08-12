def is_group(word):
    test_word = word[:]
    for i in word[:len(word)-1]:
        if test_word[test_word.count(i):].count(i) == 0:
            test_word = test_word[1:]
        else:
            return 0
    return 1

N = int(input())
cnt = 0
words = []
for _ in range(N):
    word = input()
    words.append(word)

for i in words:
    if is_group(i):
        cnt += 1

print(cnt)