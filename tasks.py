# 1- Определить, позицию второго вхождения строки в списке либо сообщить,
#  что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу",
#  ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1

# new_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# find = "йцу"
# results = list([i for i, element in enumerate(new_list) if element==find]+[-1,-1])[1]
# print(f'{new_list}, ищем: "{find}", ответ: {results}')


# 2- Найти произведение пар чисел в списке. Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.

# some_list = [4,2,3,5,6,7]

# def multip (lst):
#     new_list = []
#     for (k,j) in zip(lst [0: int(len(lst)/2+1): 1], 
#     lst [-1: int(len(lst)/2-1): -1]):
#        new_list.append(k*j)
#     return new_list

# print(f"Произведение пар чисел в списке равна: {multip(some_list)}")



# 3-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# number = int(input("Введите число: "))
# lst = [(-3)**i for i in range(number)]
# print(f"Список из N членов последовательности: {lst}")



# 5 - Есть список случайных чисел в промежутке от 1 до 100, количеством 
# 200. Создайте список кортежей, первый элемент которого - индекс 
# элемента, а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]
# import random 

# randomlist = [1,1,1,1]
# result = [(i, k) for i, k in enumerate(randomlist) if i!=k]
# print(result)


# randomlist = [random.randint(1,100) for i in range(200)]
# result = [(i, k) for i, k in enumerate(randomlist) if i!=k]
# print(result)


   

# 6 - Из списка выше оставьте только те пары, где сумма кортежа 
# кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

# randomlist = [random.randint(1,100) for i in range(200)]
# tuple_sum = list(filter(lambda x:(x[0]+x[1])%5==0,enumerate(randomlist)))
# print(f'Список пар, где сумма кортежа кратна => {tuple_sum}')

# 4 - Дан список URL различных сайтов. Нужно составить список
#  доменных имен сайтов

url_list = ["https://www.novakid.ru/education/schoolchildren/",
"https://www.libreoffice.org/about-us/who-are-we/", 
"https://www.mos.ru/pgu/ru/services/procedure/0/0/7700000010000187206/"]
 
domen_list = list(map(lambda i: i[:i.find('/')], 
[i for i in map(lambda i:i.replace('https://',''),url_list)]))
print(domen_list)

