# 2. Напишите программу, которая считает, сколько раз каждая цифра встречается в числе. Гарантируется, что на вход подаются только положительные целые числа, не выходящие за диапазон int.

num = input()
added = set()
counter = dict()
for i in num:
    if i not in counter:
        counter[i] = 1
    else:
        counter[i] += 1
print(counter)