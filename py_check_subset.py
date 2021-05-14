num_cases = int(input())

i = 0

while i < num_cases:
    num_set_a = int(input())
    set_a = set(input().split())
    # print(set_a)

    num_set_b = int(input())
    set_b = set(input().split())

    print(len(set_a.intersection(set_b)) == num_set_a)

    i += 1
