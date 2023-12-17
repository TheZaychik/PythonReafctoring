def get_account(social_security_number):
    return social_security_number if social_security_number == "123-45-6789" else None


def withdraw_money(account_number):
    print(f"Снятие денег с {account_number}")


def found_no_account():
    print("Аккаунт не найден")


# Вариант 1
account_number = get_account("123-45-6789")
if account_number:
    withdraw_money(account_number)
else:
    found_no_account()

# Вариант 2
if account_number := get_account("123-45-6789"):
    withdraw_money(account_number)
else:
    found_no_account()
