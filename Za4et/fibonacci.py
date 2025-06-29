# 3. Реализуйте генератор fibonacci(n), который будет выдавать n чисел из последовательности Фибоначчи.
# for num in fibonacci(6):
#    print(num)

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(int(input())):
    print(num)