# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, 
# вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

def Input():
    number  = input('Введите номер билета: ')
    return number

def Check(number):
    sum_first = 0
    sum_second = 0
    number_revers = number[::-1]

    for i in range(3): 
        sum_first += int(number[i])
        sum_second += int(number_revers[i])

    if sum_first == sum_second:
        print(f'{number} ---> YES')
    else:
        print(f'{number} ---> NO')

Check(Input())