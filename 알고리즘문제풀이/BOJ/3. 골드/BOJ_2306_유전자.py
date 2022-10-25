DNA = input()
L = len(DNA)
possibles = []
visited = [0] * L
opener = ['a', 'g']
closer = ['t', 'c']

for i in range(L):
    if DNA[i] in opener:
        partner = closer[opener.index(DNA[i])]
        for j in range(i+1, L):
            if DNA[j] == partner:
                visited[j] = 1
                possibles.append((i, j))

print(possibles)