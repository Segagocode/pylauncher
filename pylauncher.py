# Цвета для терминала (ANSI-коды)
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

def print_colored(text, color=Colors.RESET):
    """Выводит цветной текст"""
    print(f"{color}{text}{Colors.RESET}")

def calculator():
    operations = {
        "-": ("вычитание", lambda a, b: a - b),
        "+": ("сложение", lambda a, b: a + b),
        "/": ("деление", lambda a, b: a / b),
        "//": ("целочисленное деление", lambda a, b: a // b),
        "%": ("процент от числа", lambda a, b: a - (a * b / 100)),
        "*": ("умножение", lambda a, b: a * b),
        "**": ("возведение в степень", lambda a, b: a ** b),
    }
    
    while True:
        print_colored("\n=== КАЛЬКУЛЯТОР ===", Colors.CYAN + Colors.BOLD)
        print_colored("Доступные операции:", Colors.YELLOW)
        
        for op, (desc, _) in operations.items():
            print(f"  {op} - {desc}")
        
        print_colored("  x/exit - выйти", Colors.RED)
        
        z = input("\nВыберите знак: ").strip()
        
        if z in ("x", "exit"):
            break
        
        # Проверка на пасхалку
        if "S" in z or "s" in z:
            print_colored("Посхалко!!", Colors.YELLOW)
            continue
        
        if z not in operations:
            print_colored("Неверная операция!", Colors.RED)
            continue
        
        # Ввод чисел
        try:
            a = float(input("Первое число: "))
            b = float(input("Второе число: "))
        except ValueError:
            print_colored("Ошибка: введите корректное число!", Colors.RED)
            continue
        
        # Вычисление
        desc, func = operations[z]
        try:
            result = func(a, b)
            print_colored(f"\nРезультат ({desc}): {result}", Colors.GREEN + Colors.BOLD)
        except ZeroDivisionError:
            print_colored("Ошибка: на ноль делить нельзя!", Colors.RED)

print_colored("Добро пожаловать в PyLauncher", Colors.CYAN + Colors.BOLD)
while True:
    print_colored("\n=== МЕНЮ ===", Colors.YELLOW)
    print("1 - Калькулятор")
    print("2 - Сапёр (Beta)")
    print_colored("x/exit - Выйти", Colors.RED)

    choice = input("\nВыберите программу: ").strip()
    if choice == "1":
        calculator()
    elif choice == "2":
        print_colored("Сапёр: Beta - скоро будет доступен!", Colors.YELLOW)
    elif choice in ("x", "exit"):
        print_colored("До свидания!", Colors.GREEN)
        break
    else:
        print_colored("Неверный выбор!", Colors.RED)
