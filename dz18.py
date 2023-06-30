# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = 5
# 1 2 3 4 5
# x = 6
# -> 5

N = abs(int(input('Kol-vo elementov A: ')))
A_entered = input("Elementy: ").split()
A_num = list(map(int, A_entered))
if len(A_num) != N or N == 0:
    print('Nevernyi vvod')
else:
    X = int(input('Kakoe chislo naity: '))
    min = abs(X - A_num[0])
    index = 0
    for i in range(1, N):
        count = abs(X - A_num[i])
        if count < min:
            min = count
            index = i
    print(f'Chislo {A_num[index]} v spiske A naibolee blisko k {X}, ih raznica {abs(X - A_num[index])}')
    