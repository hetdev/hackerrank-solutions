set_a = set(input().split())
num_sets = int(input())
i = 0
resp = []
while i < num_sets:
    set_b = set(input().split())
    resp.append(
        len(set_b.intersection(set_a)) == len(set_b) and len(set_a) > len(set_b)
    )

    i += 1
print(all(resp))
