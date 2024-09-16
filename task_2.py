print('Задача 2. Функция максимума\n')

# Юра пишет различные полезные функции для Python, чтобы остальным программистам стало проще работать.
# Он захотел написать функцию, которая будет находить максимум из перечисленных чисел.
# Функция для нахождения максимума из двух чисел у него уже есть. Юра задумался: может быть,
# её можно как-то использовать для нахождения максимума уже от трёх чисел?

# Помогите Юре написать программу, которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.

# По итогу в программе должны быть реализованы две функции:
# 1) maximum_of_two — функция принимает два числа и возвращает одно (наибольшее из двух);
# 2) maximum_of_three — функция принимает три числа и возвращает одно (наибольшее из трёх);
# при этом она должна использовать для сравнений первую функцию maximum_of_two.

def maximum_of_two(a, b):
    return a if a > b else b

def maximum_of_three(a, b, c):
    return maximum_of_two(a, maximum_of_two(b, c))


first_num = int(input("Первое число: "))
second_num = int(input("Второе число: "))
third_num = int(input("Третье число: "))

print("Максимальное число:", maximum_of_three(first_num, second_num, third_num))
