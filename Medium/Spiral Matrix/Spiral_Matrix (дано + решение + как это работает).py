# Spiral Matrix

# Условие задачи:
# дана матрица размера m x n. Верните все элементы матрицы в спиральном порядке.

# Пример 1:
# входные данные: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Выходные данные: [1,2,3,6,9,8,7,4,5]

# Пример 2:
# входные данные: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Выходные данные: [1,2,3,4,8,12,11,10,9,5,6,7]

# Ограничения:
# m == количество строк в матрице
# n == количество столбцов в матрице
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix or not matrix[0]:
            return []

        result = []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left -1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top -1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

# Решение задачи обхода матрицы по спирали.

# Как работает алгоритм?

# 1. Заводим начальные границы обхода:
#   - top = 0 (верхняя строка),
#   - bottom = последняя строка,
#   - left = 0 (левый столбец),
#   - right = последний столбец.

# 2. Цикл обхода: пока верхняя граница не превысит нижнюю и левая не превысит правую:
#   - вправо: проходим по верхней строке от left до right,
#   - вниз: проходим по правому столбцу от top+1 до bottom,
#   - влево: если есть есть строки, проходим по нижней строке от right-1 до left,
#   - вверх: если есть столбцы, проходим по левому столбцу от bottom-1 до top+1.

# 3. Временная сложность: O(m x n), где m и n - размеры матрицы.

# 4. Пространственная сложность: O(1), не считая выходного массива.