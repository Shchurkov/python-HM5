# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def power(A, B):
#     if B == 0:
#         return 1
#     return A * power(A, B - 1)
# A = int(input())
# B = int(input())
# print(power(A, B))

#Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
#Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# def sum(a, b):
#     if b == 0:
#         return a
#     return sum(a + 1, b - 1)

# a = int(input())
# b = int(input())

# print(sum(a, b))