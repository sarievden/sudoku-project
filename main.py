def print_grid(grid):
    """Печатает текущее состояние сетки."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
    print()


def is_valid_move(grid, row, col, num, size):
    """
    Проверяет, можно ли вставить число num в ячейку grid[row][col].
    Возвращает True, если ход допустим, иначе False.
    """
    # Проверка строки
    if num in grid[row]:
        return False
    # Проверка столбца
    if num in [grid[i][col] for i in range(size)]:
        return False
    # Проверка квадранта
    box_size = int(size ** 0.5)
    start_row, start_col = box_size * (row // box_size), box_size * (col // box_size)
    for i in range(start_row, start_row + box_size):
        for j in range(start_col, start_col + box_size):
            if grid[i][j] == num:
                return False
    return True


def get_possible_values(grid, row, col, size):
    """
    Возвращает список всех возможных чисел для ячейки grid[row][col].
    """
    if grid[row][col] != 0:  # Если ячейка уже заполнена
        return []

    possible_values = []
    for num in range(1, size + 1):
        if is_valid_move(grid, row, col, num, size):
            possible_values.append(num)
    return possible_values
    

def is_sudoku_complete(grid):
    """Проверяет, заполнена ли сетка полностью."""
    return all(all(cell != 0 for cell in row) for row in grid)


def sudoku_game():
    """Позволяет пользователю решать Судоку с подсказками."""
    # Начальная сетка
    grid = [
        [1, 2, 3, 4],
        [4, 3, 0, 2],
        [3, 4, 2, 0],
        [2, 1, 4, 0]
    ]

    print("Начальная сетка:")
    print_grid(grid)

    while not is_sudoku_complete(grid):
        try:
            print("Введите координаты пустой клетки, чтобы получить подсказки.")
            row = int(input("Введите номер строки (1-4): ")) - 1
            col = int(input("Введите номер столбца (1-4): ")) - 1

            if grid[row][col] != 0:
                print("Эта ячейка уже заполнена! Выберите другую.")
                continue

            # Показать возможные варианты
            possible_values = get_possible_values(grid, row, col)
            if possible_values:
                print(f"Возможные значения для ячейки ({row + 1}, {col + 1}): {possible_values}")
            else:
                print(f"Нет доступных значений для ячейки ({row + 1}, {col + 1}). Проверьте введённые числа!")

            # Предложить пользователю сделать ход
            num = int(input("Введите число (1-4): "))

            if num not in possible_values:
                print("Недопустимый ход. Это число нарушает правила Судоку.")
                continue

            # Вставляем число в сетку
            grid[row][col] = num
            print("Обновлённая сетка:")
            print_grid(grid)
        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите корректные значения.")
        except IndexError:
            print("Координаты вне диапазона! Введите значения от 1 до 4.")

    print("Поздравляем! Судоку решено!")
    print_grid(grid)


if __name__ == "__main__":
    sudoku_game()
