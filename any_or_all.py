n, n_list = list(input()), list(input().split(" "))
n_positive = (all(list(map(lambda v: False if int(v) < 0 else True, n_list)))) and (
    any(list(map(lambda v: True if v == v[::-1] else False, n_list)))
)
print(n_positive)
