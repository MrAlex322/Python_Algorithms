# создать list с рандомно заполненными элементами от 0-100
# a) найти и вывести все четные элементы в нем
# b*) в dict создан выше найти все значения ключей, которые соответствуют значениям в сгенерированном list
# Например: dict={'a':0, 'd':3} list = [1,3,20] - 'd'

from random import randint

numbers = []
for i in range(10):
    numbers.append(randint(0, 30))
print(numbers)

for j in numbers:
    if j % 2 == 0:
       print(j, end = " ")

d = {
    'a': 0, 'b': 1, 'c': 2,'d': 3,'e': 4,
'f': 5,'g': 6,'h': 7,'i': 8,'k': 9,
'l': 10,'m': 11,'n': 12,'o': 13,'p': 14,
'q': 15,'r': 16,'s': 17,'t': 18,'v': 19,
'x': 20,'y': 21,'z': 22
}

for i in d :
    for j in numbers:
      if  j == d[i] :
        print(i, end = " ")