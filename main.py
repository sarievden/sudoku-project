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
