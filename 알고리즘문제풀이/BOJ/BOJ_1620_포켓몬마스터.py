import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}

for i in range(1, n+1):
    a = input().strip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    question = input().strip()
    if question.isdigit():
        print(dict[int(question)])
    else:
        print(dict[question])