print("Добро пожаловать в PyLauncher")

while True:
    pyl = input("введите номер программы: ")
    if pyl == ("1"):
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
            if z == ("x"):
                break
            a = input("Выберите первое число: ")
            b = input("Выберите второе число: ")
            if "." in a:
                a = float(a)
            else:
                a = int(a)
            if "." in b:
                b = float(b)
            else:
                b = int(b)

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
    #--------------------------------------------------#
    elif pyl == 2:
        print("Сапёр: Beta")
    #-----------------------------------------------
    elif pyl == ("x"):
        break
