import os # Используется только для очистки консоли
import subprocess # Используется только для очистки консоли

def rpn_evaluate(expression):
    tokens = expression.split() # Чтение выражения
    stack = []
    
    # Exception: Если строка пустая
    if not tokens:
        return "Ошибка: Введена пустая строка."
        
    for token in tokens:
        if token in ('+', '-', '*', '/'):
            # Exception: В стеке меньше двух чисел
            if len(stack) < 2:
                return f"Ошибка: Недостаточно чисел в стеке для операции '{token}'."
                
            b = stack.pop() # LIFO: второй операнд будет последним в стеке
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b) # Проверка деления на 0 не нужна, так как все числа положительные
        else:
            # Exception: Элемент не является вещественным числом
            try:
                number = float(token)
                # Exception: Число не является положительным
                # Exception: В вводе обнаружены символы которые не являются числами или знаками операций
                if number <= 0:
                    return f"Ошибка: Все числа должны быть положительными."
                stack.append(number)
            except ValueError:
                return f"Ошибка: Некорректный символ, элемент или команда: '{token}'."
                
    # Exception: В вводе обнаружены лишние числа
    if len(stack) != 1:
        extra_count = len(stack) - 1
        return f"Ошибка: Выражение составлено неверно. В стеке остались лишние числа. Количество лишних чисел: {extra_count}"
    
    return f"Ответ: {stack[0]}"

def examples(): # Вспомогательная функция: примеры ввода
    # 1. Корректный пример
    print("Пример 1: 5 2 / ", rpn_evaluate("5 2 /"))                  
    
    # 2. Корректный пример
    print("Пример 2: 5 10 2 / 2.5 / 4 * + ", rpn_evaluate("5 10 2 / 2.5 / 4 * +")) 
    
    # 3. Ошибка: Число меньше нуля
    print("Пример 3: 5 -2 + ", rpn_evaluate("5 -2 +"))                 
    
    # 4. Ошибка: Лишний оператор
    print("Пример 4: 5 3 + * ", rpn_evaluate("5 3 + *"))                
    
    # 5. Ошибка: Лишнее число
    print("Пример 5: 5 3 2 + ", rpn_evaluate("5 3 2 +"))                
    
    # 6. Ошибка: Некорректный символ
    print("Пример 6: 5 one + ", rpn_evaluate("5 one +"))

    print("Примечание для ввода: Числа и знаки выражения разделяются пробелами.")     

def clear(): # Вспомогательная функция: очистка консоли
    try:
        # В Windows ('nt') используется команда 'cls'
        if os.name == 'nt':
            subprocess.run(['cls'], shell=True, check=True)
        # В Linux и macOS используется команда 'clear'
        else:
            subprocess.run(['clear'], check=True)
    except (subprocess.SubprocessError, FileNotFoundError):
        # Если другая операционная система (Резервный метод)
        print("\n" * 100) # Вывод пустых строк
    print("Консоль очищена.")

def exit(): # Вспомогательная функция: Завершение программы
    print("Выход из программы...")
    return False

if __name__ == "__main__":
    
    print("Вычисление выражений в обратной польской записи (RPN).")

    work = True

    while work:
      expression = input("Введите выражение в обратной польской записи или команду (Введите 'help' для вызова меню команд): ")
      expression = expression.strip().lower() # Убирает лишние пробелы в начале и конце, превращает заглавные буквы в строчные

      if expression == 'help':
          print("Командное меню:")
          print("'examples' - Показать примеры ввода и итогового результата после их решения программой.")
          print("'clear' - Очистить консоль.")
          print("'exit' - Завершить программу.")
      elif expression == 'examples':
          examples()
      elif expression == 'exit':
          work = exit()
      elif expression == 'clear':
          clear()
      else:
          print(f"Ваше выражение: {expression}")
          print("Вывод:", rpn_evaluate(expression))
          ifcontinue = input("Введите 'Y' чтобы ввести ещё одно выражение, либо любой другой символ для выхода: ")
          if ifcontinue.lower() != 'y':
              work = exit()
    print("Программа завершена.")