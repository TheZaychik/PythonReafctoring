students = ['Иван', 'Маша', 'Олег', 'Дарья']
# Вариант 1
for i in range(len(students)):
    student = students[i]
    print(f"# {i + 1}: {student}")
# Вариант 2
for i, student in enumerate(students, 1):
    print(f"# {i}: {student}")
