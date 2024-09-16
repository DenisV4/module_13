print('Задача 3. Число наоборот 2\n')

# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример:

# Введите первое число: 102
# Введите второе число: 123


# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225

def reverse_number(number):
    return int(str(number)[::-1].lstrip("0"))

first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))
print()

print("Первое число наоборот:", reverse_number(first_num))
print("Второе число наоборот:", reverse_number(second_num), "\n")
print("Сумма:", reverse_number(first_num) + reverse_number(second_num))
print("Сумма наоборот:", reverse_number(reverse_number(first_num) + reverse_number(second_num)))
