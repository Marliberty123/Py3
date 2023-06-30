# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь
# в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках
# записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3

# -> 1

N = abs(int(input('Kol-vo elementov A: ')))
A_entered = input("Elementy: ").split()
A_num = list(map(int, A_entered))
if len(A_num) != N:
    print('Nevernyi vvod')
else:
    X = int(input('Kakoe chislo naity: '))
    count = 0
    for i in range(N):
        if A_num[i] == X:
            count += 1
    print(f'Chislo {X} est v spiske A {count} raz') 
    
    
