# create a list of squares of 1 to 10

squares = [i * i for i in range(1,11)]
print(squares)

# filter passed students based on their grade

student_grades = [100, 90, 80, 70, 60, 40, 20, 0]

passed = [i for i in student_grades if i >= 60]
print(passed)

# replace all grades below 60 to word 'FAILED'

grades2 = [i if i >= 60 else 'FAILED' for i in student_grades]
print(grades2)