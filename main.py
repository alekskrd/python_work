
from functools import reduce
from random import randint
import itertools
from functools import reduce


field = range(1, 10)

def draw_field(field):
    print('-------------')
    for i in range(3):
        print('|', field[0+i*3], '|', field[1+i*3], '|', field[2+i*3], '|')
        print('-------------')

draw_field(field)





d = [1, 2, 3, 4, 5]

pr = reduce(lambda x, y: x*y, d)
print(pr)



k = 5

ratios = [randint(0, 10) for i in range(k + 1)]
while ratios[0] == 0:
    ratios[0] = randint(1, 10)

ratios = [1, 8, 2, 0, 5]



n = [n for n in range(k, -1, -1)]
pol = list(zip(ratios, n))

print(n)
print(pol)


# 38. Напишите программу, удаляющую из 
# текста все слова содержащие "абв".

my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие "абв"'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)
