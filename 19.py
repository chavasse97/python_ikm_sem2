class TreeNode:
    def __init__(self, value=None):
        self.value = value # Значение в узле
        self.left = None # Левый потомок (0)
        self.right = None # Правый потомок (1)


def build_tree(data_pairs):
    root = TreeNode(0) # В корень заносится значение 0
    
    # Построение и проверка на перезапись
    for value, path in data_pairs:
        current = root
        
        for char in path:
            if char == '0':
                if current.left is None:
                    current.left = TreeNode()
                current = current.left
            elif char == '1':
                if current.right is None:
                    current.right = TreeNode()
                current = current.right
            else:
                raise ValueError("Недопустимый символ '" + char + "' в двоичном коде '" + path + "'")
        
        # Exception: Перезапись значения
        if current.value is not None:
            raise ValueError(
                "Обнаружена перезапись: путь '" + path + "' уже занят числом '" + 
                str(current.value) + "', невозможно записать число '" + str(value) + "'."
            )
            
        current.value = value
        
    # Проверка на наличие пустых ячеек
    check_for_empty_nodes(root.left, "0")
    check_for_empty_nodes(root.right, "1")
        
    return root


def check_for_empty_nodes(node, current_path):
    if node is None:
        return
        
    # Exception: Если узел существует, но его значение не задано
    if node.value is None:
        raise ValueError(
            "Обнаружена пустая промежуточная ячейка по пути '" + current_path + 
            "'. Дерево не может быть построено."
        )
        
    # Рекурсивная проверка потомков
    check_for_empty_nodes(node.left, current_path + "0")
    check_for_empty_nodes(node.right, current_path + "1")

def parse_line(line, line_id): # Проверка данных и преобразование строки
    line = line.strip() # Убирает лишние пробелы
    if not line:
        return None

    parts = line.split()
    if len(parts) != 2:
        print("Ошибка в записи " + str(line_id) + ": ожидалось 2 элемента, получено " + str(len(parts)))
        return None

    try:
        val = int(parts[0])
    except ValueError:
        print("Ошибка в записи " + str(line_id) + ": '" + parts[0] + "' не является целым числом")
        return None

    path = parts[1]
    return val, path


def read_from_file(): # Чтение из файла
    file_path = input("Введите имя или путь к файлу: ").strip() # Ожидается формат "file.txt"
    data_pairs = []
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            line_num = 0
            for line in file:
                line_num += 1
                parsed = parse_line(line, "в строке " + str(line_num))
                if parsed:
                    data_pairs.append(parsed)
    except FileNotFoundError: # Exception: Ошибки при открытии файла
        print("Ошибка: Файл '" + file_path + "' не найден.")
        return None
    except PermissionError:
        print("Ошибка: Нет прав на чтение файла '" + file_path + "'.")
        return None
    except Exception as e:
        print("Непредвиденная ошибка при чтении файла: " + str(e))
        return None
        
    return data_pairs


def read_from_console(): # Ввод с клавиатуры
    print("\nВыбран ручной ввод данных")
    print("Введите данные в формате: [число] [путь] через пробел")
    print("Для завершения ввода введите 0")
    print("-" * 45) # Разделитель
    
    data_pairs = []
    entry_num = 0
    
    while True:
        entry_num += 1
        try:
            line = input("Запись " + str(entry_num) + ": ").strip()
            if line == "0":
                print("Ввод завершен.")
                break
                
            parsed = parse_line(line, entry_num)
            if parsed:
                data_pairs.append(parsed)
        except Exception as e: # Exception
            print("Ошибка при вводе: " + str(e))
            
    return data_pairs


def main():
    print("Выберите способ ввода данных:")
    print("1: Прочитать данные из файла")
    print("2: Ввести вручную")
    
    choice = input("Ваш выбор: ").strip()
    data_pairs = []
    
    if choice == "1":
        data_pairs = read_from_file()
    elif choice == "2":
        data_pairs = read_from_console()
    else:
        print("Неверный выбор. Программа завершена.")
        return

    if not data_pairs:
        print("Не найдены корректные данные для построения. Сборка дерева отменена.")
        return

    try:
        tree_root = build_tree(data_pairs) # Переменная была создана для вывода дерева, функция вывода не была реализована
        print("Дерево успешно построено.")
    except ValueError as val_err:
        print("\nОшибка построения дерева " + str(val_err))
    except Exception as e:
        print("\nНепредвиденная ошибка при построении дерева: " + str(e))


if __name__ == "__main__":
    print("Построение бинарного дерева по данным из файла.")
    main()
