n_1, students_list_1 = input(), list(input().split(" "))
n_2, students_list_2 = input(), list(input().split(" "))
answer_list = list(map(lambda s: s in students_list_2, students_list_1))
print(sum(answer_list))
