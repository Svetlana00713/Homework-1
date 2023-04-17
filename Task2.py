# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

def Input():
    count = 0
    num = input('Введите трехзначное число:  ')
    if len(num) > 3 or len(num) < 3:
        print('Число не трехзначное')
        return -1
    else:
        for i in range(3):
            count += int(num[i])   
    return count        

print(Input())


