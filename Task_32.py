# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# Метод list.index(*элемент*) не использовала, так как при наличии повторений 
# он возвращает индекс первого вхождения элемента в списке, что не совсем корректно!

from random import randint

list = [randint(-20, 20) for i in range(int(input("Введите длину массива: ")))]
print(list)

min_value, max_value = int(input("Введите минимальное значение: ")), int(input("Введите максимальное значение: "))

index_list = [index for index in range(len(list)) if min_value <= list[index] <= max_value]
print(index_list)