students = ['小明', '小红', '小刚']

for i in range(0, 3):
    first_student = students.pop(0)
    students.append(first_student)
    print(students)