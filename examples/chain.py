from itertools import chain

group1 = ['Иван', 'Маша', 'Олег', 'Дарья']
group2 = ['Лёша', 'Дима', 'Никита', 'Илья']
# Вариант 1
for student in group1:
    print(student)
for student in group2:
    print(student)
# Вариант 2
for student in group1 + group2:
    print(student)
# Вариант 3 (самый экономичный по памяти)
for student in chain(group1, group2):
    print(student)
