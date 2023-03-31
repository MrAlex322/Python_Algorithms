# a) создать программу которая создает list с размером n, с рандомно заполненными элементами от a-b.
# Где параметры a, b и n задаются пользователем через консоль. Отсортировать список
# b) дать пользователю возможность ввести значение через консоль, проверить есть ли это значение в list.
# Если есть вывести true, если нету false
# c) реализовать линейный и бинарный методы поиска. Дать возможность пользователю выбрать метод поиска

# Оценить сложность алгоритма:
from random import randint

n = int(input("Введите количество элементов списка: "))
a = int(input("Введите нижнюю границу значений списка: "))
b = int(input("Введите верхнюю границу значений списка: "))

list = []
for i in range(n):
    list.append(randint(a, b))
list.sort()
print(list)

search = str(input("Выберите способ поиска 'бинарный' или 'линейный': "))

if search == "бинарный" or search == "binary":  #удалять пробелы
    
    def binary_search(list, num):

        low = 0
        high = len(list) - 1

        while low <= high:
            
            middle = (low + high)//2

            if list[middle] == num:
                return middle
            elif list[middle] > num:
                high = middle - 1
            else:
                low = middle + 1

        return -1

    res = binary_search(list, num=int(input("Введите число: ")))

    if res != -1:
        print("Элемент присутсвует в списке, с индексом", str(res))
    else:
        print("Элемент отсутсвует в списке list")

elif search == "линейный" or "linear":
    def linear_search(num):

        if num in list:
            print("True")
        else:
            print("false")

    res = linear_search(num=int(input("Введите числоё: ")))

else:
    print("Введите корректный поиск")