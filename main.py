import math

while(True):
    print("Выберите действие:")
    print("1.Сложение")
    print("2.Вычитание")
    print("3.Умножение")
    print("4.Деление")
    print("5.Возведение в степень")
    print("6.Квадратный корень")
    print("7.Факториал")
    print("8.Синус")
    print("9.Косинус")
    print("10.Тангенс")
    print("11.Выход из программы")
    c = int(input())
    if c == 1:
        print("Введите первое число:")
        a = int(input())
        print("Введите второе число:")
        b = int(input())
        print("Результат","", a+b)
    elif c == 2:
        print("Введите первое число:")
        a = int(input())
        print("Введите второе число:")
        b = int(input())
        print("Результат", "", a - b)
    elif c == 3:
        print("Введите первое число:")
        a = int(input())
        print("Введите второе число:")
        b = int(input())
        print("Результат", "", a * b)
    elif c == 4:
        print("Введите первое число:")
        a = int(input())
        print("Введите второе число:")
        b = int(input())
        if b == 0:
            print("на ноль не делят")
        else:
            print("Результат", "", a / b)
    elif c == 5:
        print("Введите число:")
        a = int(input())
        print("Введите степень:")
        b = int(input())
        print("Результат", "", a ** b)
    elif c == 6:
        print("Введите число:")
        a = int(input())
        print("Результат", "", a ** 0.5)
    elif c == 7:
        print("Введите число:")
        a = int(input())
        print("Результат", "", math.factorial(a))
    elif c == 8:
        print("Введите число в градусах:")
        a = int(input())
        a = math.radians(a)
        print("Результат", "", math.sin(a))
    elif c == 9:
        print("Введите число в градусах:")
        a = int(input())
        a = math.radians(a)
        print("Результат", "", math.cos(a))
    elif c == 10:
        print("Введите число в градусах:")
        a = int(input())
        a = math.radians(a)
        print("Результат", "", math.tan(a))
    elif c == 11:
        break
    else:
        print("боги говорят, что ты не смотришь в список и ты тупой")