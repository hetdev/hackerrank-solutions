n_1, students_list_1 = input(), set(input().split(" "))
n_2, students_list_2 = input(), set(input().split(" "))
print(len(students_list_1.symmetric_difference(students_list_2)))
