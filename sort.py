# sort() method for list
student_list = ["Yufeng", "Jane", "Steven"]
student_list.sort()

print("-------------------")
for i in student_list:
    print(i)

# sort() method for list with sort field and reverse
student_tuple_list = [
    ("Yufeng", "A", 40),
    ("Jane", "D", 38),
    ("Steven", "B", 10)
]
grade = lambda grades:grades[1]
student_tuple_list.sort(key=grade, reverse=True)

print("-------------------")
for i in student_tuple_list:
    print(i)

# sorted() function for iterables
student_tuple = ("Yufeng", "Jane", "Steven")
sorted_students_tuple = sorted(student_tuple)

print("-------------------")
for i in sorted_students_tuple:
    print(i)

# sorted() function for iterables with sort field
student_tuple_tuple = (
    ("Yufeng", "A", 40),
    ("Jane", "D", 38),
    ("Steven", "B", 10)
)

age = lambda ages:ages[2]
sorted_student_tuple_tuple = sorted(student_tuple_tuple, key = age)

print("-------------------")
for i in sorted_student_tuple_tuple:
    print(i)