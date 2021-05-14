from itertools import permutations

inputt = input().split()
for prod in sorted(list(permutations(inputt[0], int(inputt[1])))):
    print("".join(prod))
