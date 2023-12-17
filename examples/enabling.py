some_numbers = list(range(10))
print(some_numbers)
# Вариант 1
even_numbers = []
for num in some_numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)
# Вариант 2
even_numbers = [num for num in some_numbers if num % 2 == 0]
print(even_numbers)
