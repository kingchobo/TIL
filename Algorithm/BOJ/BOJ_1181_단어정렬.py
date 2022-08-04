N = int(input())

words_list = []
for i in range(N):
    word = input()
    if (len(word), word) in words_list:
        pass
    else:
        words_list.append((len(word), word))
words_list.sort(key=lambda x : (x[0], x[1]))

for j in words_list:
    print(j[1])