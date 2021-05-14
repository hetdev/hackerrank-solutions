from itertools import product

a = [int(i) for i in (input().split())]
b = [int(i) for i in (input().split())]
srt = ""
for prod in tuple(product(a, b)):
    srt += f"{prod} "
print(srt)
