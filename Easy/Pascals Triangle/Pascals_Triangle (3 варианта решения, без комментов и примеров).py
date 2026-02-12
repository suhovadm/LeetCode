# Треугольник Паскаля. Все варианты решений.

# Вариант #1, более явное разделение.

from typing import List

class Solution:
    def generation(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        triangle = []

        for i in range(numRows):
            current_row = [1] * (i + 1)

            if i >= 2:
                for j in range(1, i):
                    current_row[j] = triangle[i-1][j-1] + triangle[i-1][j]

            triangle.append(current_row)

        return triangle

# -------------------------------------------------------------------------------

# Вариант 2, более лаконичная версия.

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        triangle = []

        for i in range(numRows):

            row = []

            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(triangle[i-1][j-1] + triangle[i-1][j])
                triangle.append(row)

        return triangle

# -------------------------------------------------------------------------------

# Вариант 3, самый простой вариант.

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        triangle = []

        for i in range(numRows):

            row = [1] * (i + 1)

            for j in range(1, i):
                prev_row = triangle[i-1]
                row[j] = prev_row[j-1] + prev_row[j]

            triangle.append(row)

        return triangle
