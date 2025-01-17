import unittest
from src.lab3.sudoku import create_grid, group, get_row, get_col, get_block, find_empty_positions, find_possible_values, \
    check_position_is_safe, solve, check_solution, generate_random_grid, delete_cells, generate_sudoku


class SudokuTestCase(unittest.TestCase):

    def test_group(self):
        """
        Тест написанной функции group
        Функция должна группировать значения списка values в список, состоящий из списков по n элементов
        """
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8], 2), [[1, 2], [3, 4], [5, 6], [7, 8]])
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8], 2), [[1, 2], [3, 4], [5, 6], [7, 8]])
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 4),
                         [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 1), [[1], [2], [3], [4], [5], [6], [7], [8], [9]])

    def test_get_row(self):
        """
        Тест написанной функции get_row
        Функция возвращает все значения для номера столбца, указанной в pos
        """
        self.assertEqual(get_row([['1', '2'], ['3', '4'], ['5', '6'], ['7', '8'], ['9', '10']], (0, 0)), ['1', '2'])
        self.assertEqual(get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)), ['1', '2', '.'])
        self.assertEqual(get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0)), ['4', '.', '6'])
        self.assertEqual(get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0)), ['.', '8', '9'])

    def test_get_col(self):
        """
        Тест написанной функции get_col
        Функция возвращает все значения для номера строки, указанной в pos
        """
        self.assertEqual(get_col([['1', '2'], ['3', '4'], ['5', '6'], ['7', '8'], ['9', '10']], (0, 0)),
                         ['1', '3', '5', '7', '9'])
        self.assertEqual(get_col([['1', '2'], ['3', '4'], ['5', '6'], ['7', '8'], ['9', '10']], (0, 1)),
                         ['2', '4', '6', '8', '10'])
        self.assertEqual(get_col([['.', '2', '3'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)), ['.', '4', '7'])
        self.assertEqual(get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1)), ['2', '.', '8'])
        self.assertEqual(get_col([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '.']], (0, 2)), ['3', '6', '.'])

    def test_get_block(self):
        """
        Тест написанной функции get_block
        Функция возвращает все значения в квадрате 3 на 3
        """
        grid = create_grid("53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79")
        self.assertEqual(get_block(grid, (0, 0)), ['5', '3', '.', '6', '.', '.', '.', '9', '8'])
        self.assertEqual(get_block(grid, (1, 1)), ['5', '3', '.', '6', '.', '.', '.', '9', '8'])
        self.assertEqual(get_block(grid, (2, 2)), ['5', '3', '.', '6', '.', '.', '.', '9', '8'])
        self.assertEqual(get_block(grid, (4, 7)), ['.', '.', '3', '.', '.', '1', '.', '.', '6'])
        self.assertEqual(get_block(grid, (8, 8)), ['2', '8', '.', '.', '.', '5', '.', '7', '9'])

    def test_find_empty_positions(self):
        """
        Тест написанной функции find_empty_positions
        Функция должна найти первую пустую позицию в пазле и вернуть её координаты
        """
        self.assertEqual(find_empty_positions([['.', '2'], ['3', '4'], ['5', '6'], ['7', '8'], ['9', '10']]), (0, 0))
        self.assertEqual(find_empty_positions([['1', '2'], ['3', '.'], ['5', '6'], ['7', '8'], ['9', '10']]), (1, 1))
        self.assertEqual(find_empty_positions([['1', '2'], ['3', '4'], ['5', '6'], ['7', '8'], ['.', '10']]), (4, 0))
        self.assertEqual(find_empty_positions([['.', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]), (0, 0))
        self.assertEqual(find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']]), (1, 1))
        self.assertEqual(find_empty_positions([['1', '2', '3'], ['4', '5', '.'], ['7', '8', '9']]), (1, 2))
        self.assertEqual(find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']]), (2, 0))
        self.assertEqual(find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '.']]), (2, 2))

    def test_find_possible_values(self):
        """
        Тест написанной функции find_possible_values
        Функция возвращает список элементов, которые можно использовать в качестве подстановки на пустое место
        - элементы не повторяются ни в строке, ни в столбце, ни в квадрате
        """
        grid = create_grid("53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79")
        self.assertEqual(find_possible_values(grid, (0, 2)), {'1', '2', '4'})
        self.assertEqual(find_possible_values(grid, (4, 7)), {'2', '5', '9'})

    def test_check_position_is_safe(self):
        """
        Тест написанной функции check_position_is_safe
        Возвращает 1 если на заданное место можно поставить заданный элемент, 0 если нет
        """
        grid = create_grid("53..7....6.1195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79")
        self.assertEqual(check_position_is_safe(grid, (0, 2), "4"), True)
        self.assertEqual(check_position_is_safe(grid, (0, 2), "1"), False)

    def test_check_solution(self):
        """
        Тест написанной функции check_solution
        Функция проверяет не повторяется ли каждое значение в столбце, строке, квадрате
        """
        solution1 = [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
                     ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
                     ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
                     ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
                     ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
        solution2 = [['3', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
                     ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
                     ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
                     ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
                     ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
        self.assertEqual(check_solution(solution1), True)
        self.assertEqual(check_solution(solution2), False)
