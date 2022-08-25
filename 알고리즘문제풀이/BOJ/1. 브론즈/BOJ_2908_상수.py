A, B = input().split()
reversed_A = "".join(reversed(A))
reversed_B = "".join(reversed(B))

print(reversed_B if int(reversed_B) > int(reversed_A) else reversed_A)