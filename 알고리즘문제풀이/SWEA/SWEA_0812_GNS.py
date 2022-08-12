T = int(input())
for tc in range(1, T+1):
    _, __ = input().split()
    word_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    word = list(input().split())
    new_list = []

    for i in word:
        new_list += [word_list.index(i)]

    print(f'#{tc}')

    # 순서대로 출력
    for i in range(10):
        for j in range(int(__)):
            if new_list[j] == i:
                print(word_list[i], end=' ')