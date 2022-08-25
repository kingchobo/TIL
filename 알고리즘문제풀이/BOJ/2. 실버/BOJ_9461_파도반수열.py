import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    p_list = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12]

    def p(n):
        if n <= 11:
            return p_list[n]
        else:
            i = 12
            while i <= n:
                p_list.append(p_list[i-1] + p_list[i-5])
                i += 1
            return p_list[n]
    print(p(n))