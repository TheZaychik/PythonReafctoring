# Задача: ОТРЕФАКТОРИТЬ КОД ПО ПОЛНОЙ ПРОГРАММЕ ))) ))) )))
def some_function(numbers: list[int]) -> None:
    if len(numbers) == 0:
        return
    print("Вы ввели массив, который начинается с {0}".format(numbers[0]))
    div_by_5 = []
    for num in numbers:
        if num % 5 == 0:
            div_by_5.append(num)
    print(div_by_5)
    first_number = numbers[0]
    middle_numbers = numbers[1:-1]
    last_number = numbers[-1]
    print(first_number, middle_numbers, last_number)
    for num in numbers:
        print(num)
    for num in div_by_5:
        print(num)
