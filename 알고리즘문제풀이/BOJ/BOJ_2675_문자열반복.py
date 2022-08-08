def solve(n, word):
    new_str = ''
    for char in word:
        new_str += char * n
    return(new_str)

T = int(input())

for case in range(T):
    n, word = input().split()
    print(solve(int(n), word))