#Данно массив из n положительных целых чисел и целевое значение s,
# найдите наименьший подмассив, сумма которого больше или равна s. Если такого подмассива нет, вернуть 0.


lst = [2, 4, 3, 7, 6, 8, 9]
num = int(input("Введите число: "))

def sliding_window(elements, window_size):
    min_mass = []
    if len(elements) <= window_size:
        return elements
    for i in range(len(elements) - window_size + 1):
        f = sum(elements[i:i + window_size])
        if num <= sum(elements[i:i + window_size]):
            min_mass = elements[i:i + window_size]
            # if sum(elements[i:i + window_size]) <= sum(min_mass):
            #     min_mass = elements[i:i + window_size]
    print(min_mass)

sliding_window(lst, 3)
