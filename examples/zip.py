students = ['Иван', 'Маша', 'Олег', 'Дарья']
marks = [5, 4, 3, 4]
# Вариант 1
marks_tracking = {}
for i in range(min(len(students), len(marks))):
    marks_tracking[students[i]] = marks[i]
print(marks_tracking)
# Вариант 2
marks_tracking = dict(zip(students, marks))
print(marks_tracking)