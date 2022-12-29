# Вычислить число c заданной точностью d
# Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# n = int(input('Enter your degree of accuracy for PI: '))
# k = 1
# s = 0
# for i in range ( 10000 ):
#     if i % 2 == 0:
#         s += 4 / k
#     else :
#         s -= 4 / k
#     k += 2

# print (round(s,n))

#Задайте натуральное число N. Напишите программу, 
#которая составит список простых множителей числа N.

# num = int(input("Enter your N: "))
# my_num = 2  
# lst = []
# old = num
# while my_num <= num:
#     if num % my_num == 0:
#         lst.append(my_num)
#         num //= my_num
#         my_num = 2
#     else:
#         my_num += 1
# print(f"My multipliers of a number  {old} in the list: {lst}")


# 3 Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной 
# последовательности.

# n = list(map(int,input('Enter your numbers interval: ').split()))
# def get_unique_numbers(n):
#     unique = [] 
#     for n in n:
#         if n in unique:
#             continue
#         else:
#             unique.append(n)
#     return unique
# print(get_unique_numbers(n))


#Задана натуральная степень k. Сформировать случайным образом 
#список коэффициентов (значения от 0 до 100) многочлена и записать 
#в файл многочлен степени k.
#*Пример:* 
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# НЕ Успел -Happy New Year !!!


# 5 Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# # НЕ Успел -Happy New Year !!!