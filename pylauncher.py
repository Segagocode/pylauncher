def calculator():
    while True:
        print("Запущен калькулятор")
        z = input("Выберите знак (-, +, /, //, *, **): ")
        print("- - вычитание")
        print("+ - сложение")
        print("/ - деление")
        print("// - деление с остатком")
        print("% - вычесть процент")
        print("* - умножить")
        print("** - возвести в степень")
        print("x/exit - выйти из калькулятора")
        if z == ("x") or z == ("exit"):
            break
        a = input("Выберите первое число: ")
        b = input("Выберите второе число: ")
        if "." in a:
            try:
                a = float(a)
            except ValueError:
                print("Ошибка: Введите корректное число")
                continue
        else:
            try:
                a = int(a)
            except ValueError:
                print("Ошибка: Введите корректное число")
                continue
        if "." in b:
            try:
                b = float(b)
            except ValueError:
                print("Ошибка: Введите корректное число")
                continue
        else:
            try:
                b = int(b)
            except ValueError:
                print("Ошибка: Введите корректное число")
                continue

        if z == "-":
            c = a - b
            print(c)
        elif z == "+":
            c = a + b
            print(c)
        elif z == "/":
            try:
                c = a / b
                print(c)
            except ZeroDivisionError:
                print("на ноль не делиться")
        elif z == "//":
            try:
                c = a // b
                print(c)
            except ZeroDivisionError:
                print("на ноль не делиться")
        elif z == "%":
            c = a - (a * b / 100)
            print(c)
        elif z == "*":
            c = a * b
            print(c)
        elif z == "**":
            c = a ** b
            print(c)
        elif "S" in z or "s" in z:
            print("Посхалко!!")
        else:
            print('Не введена исполняемая операция')

print("Добро пожаловать в PyLauncher")
while True:
    print("1 - Калькулятор")
    print("2 - Сапёр")
    print("x/exit - Выйти")

    choice = input("Выберите программу: ")
    if choice == "1":
        calculator()
    elif choice == "2":
        print("Сапёр: Beta")
    elif choice == "x" or choice == "exit":
        break
    else:
        print("Неверный выбор")
    #--------------------------------------------------#
