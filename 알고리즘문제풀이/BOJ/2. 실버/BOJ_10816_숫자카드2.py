import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
N_dict = {}
for i in N_list:
    if i not in N_dict:
        N_dict[i] = 1
    else:
        N_dict[i] += 1
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

for i in M_list:
    if i in N_dict:
        print(N_dict[i], end=' ')
    else:
        print(0, end=' ')