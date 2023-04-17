# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
#  Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
#  если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

def Input():
    s = int(input('Введите общее количество журавликов: '))
    return s

def Result(s):
    petya = sergey = (s // 3) // 2
    katya = s - (petya + sergey)
    print(f'Катя сделала {katya} журавликов')
    print(f'Сергей сделал {sergey} журавликов')
    print(f'Петя сделал {petya} журавликов')

Result(Input())