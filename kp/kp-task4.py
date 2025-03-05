"""
Задача4
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

string = input()
substring = input()
counter = 0
for i in range (len(string)):
    if string[i:i+len(substring)] == substring:
        counter += 1
print(counter)