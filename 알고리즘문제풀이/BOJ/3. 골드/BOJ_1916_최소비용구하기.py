import sys

N = int(sys.stdin.readline())
cities = [0] * (N+1)
buses = [[] for _ in range(N+1)]
costs = [[] for _ in range(N+1)]

M = int(sys.stdin.readline())
for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    buses[start].append(end)
    costs[start].append(cost)

S, E = map(int, sys.stdin.readline().split())

dp = [0] * (N+1)
for i in range(S, E+1):
