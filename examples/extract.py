some_numbers = tuple(range(10))
print(some_numbers)
# Вариант 1
first_number = some_numbers[0]
middle_numbers = some_numbers[1:-1]
last_number = some_numbers[-1]
print(first_number, middle_numbers, last_number)
# Вариант 2
first_number, *middle_numbers, last_number = some_numbers
print(first_number, middle_numbers, last_number)
# Задача со звездочкой :) - обратить внимание на вывод скрипта
