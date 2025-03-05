""" Задача 1.
Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. 
Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.
Напишите программу, на вход которой даются четыре числа a, b, c и d - каждое в своей строке. 
Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a;b] на все числа отрезка [c;d]

Sample Input 1:
7
10
5
6
Sample Output 1:

	5	6
7	35	42
8	40	48
9	45	54
10	50	60
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print("\t")
for i in range (c, d+1):
    print(i, end = "\t")
print()

for i in range (a, b+1):
    print(i, end = "\t")
    for j in range (c, d+1):
        print(i*j, end = "\t")
    print()

"""Задача2
В Институте биоинформатики между информатиками и биологами устраивается соревнование.
Победителям соревнования достанется большой и вкусный пирог.
В команде биологов a человек, а в команде информатиков — b человек.
Нужно заранее разрезать пирог таким образом, чтобы можно было раздать кусочки пирога любой команде, 
выигравшей соревнование, при этом каждому участнику этой команды должно достаться одинаковое число кусочков пирога.
И так как не хочется резать пирог на слишком мелкие кусочки, нужно найти минимальное подходящее число.

Sample Input 1:
7
5
Sample Output 1:
35

Sample Input 2:
15
15
Sample Output 2:
15
"""

a = int(input())
b = int(input())
m = a * b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print(m // (a + b))

"""Задача4
На вход программе подается два строковых значения разделенных пробелом: string и substring. 
Не используя готовые методы строк (count и аналогичные) подсчитайте, сколько раз во введенной строке 
string встречается подстрока substring. В качестве ответа распечатайте число: количество вхождении.

Sample Input 1:

abaaa
a
Sample Output 1:

4
Sample Input 2:

abbaba
ab
Sample Output 2:

2
"""
s = input()
sb = input()
c = 0

for i in range (len(s)):
    if s[i:i+len(sb)] == sb:
        c += 1
print(c)

"""Задача3
Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики 
студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.
Кодирование осуществляется следующим образом: s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых 
символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.
Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную 
последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.
"""
a = input()
l = len(a)
i = -1
s = ""
while l != 0:
    с = 0
    i += 1
    s += a[i]
    while a[i] == a[i+1]:
        c += 1
        l -= 1
    s += str(c)
print(s)

#не работает, не могу понять в чем ошибка и как исправить. вообщем как заставить ее работать
