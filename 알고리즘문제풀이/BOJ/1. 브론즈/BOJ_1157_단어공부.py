given_word = input().lower()
word_list = list(set(given_word))
cnt = []

for i in word_list:
    count = given_word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(word_list[cnt.index(max(cnt))].upper())