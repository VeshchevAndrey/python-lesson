def calculate(operation, a, b):
    if operation == '+': return a + b
    elif operation == '-': return a - b
    elif operation == '*': return a * b
    elif operation == '/':
        return a / b
    elif operation == '**': return a ** b
    else:
        return "Неизвестная операция"  

while True:
    try:
       op = input("Операция (+,-,*,/,** или 'exit'): ")
       if op == 'exit': break
       x = float(input("Первое число: "))
       y = float(input("Второе число: "))
       result = calculate(op, x, y)
       print(f"Результат: {result}")
    except Exception as e:
        print(f"СБОЙ! Ошибка: {type(e).__name__}")
