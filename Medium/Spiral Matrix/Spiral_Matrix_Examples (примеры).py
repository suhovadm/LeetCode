from Spiral_Matrix import *

# Создаем экземпляр класса Solution.
solution = Solution()

# Пример 1.
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
print('Пример 1:')
print('входная матрица:')
for row in matrix1:
    print(row)
print('Результат обхода по спирали:')
print('заканчивается на 5, т.е. выходим на 5.')
print(solution.spiralOrder(matrix1))
print()

# Пример 2.
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print('Пример 2:')
print('входная матрица:')
for row in matrix2:
    print(row)
print('Результат обхода по спирали:')
print('заканчивается на 7, т.е. выходим на 7.')
print(solution.spiralOrder(matrix2))
print()

# Дополнительный пример.
matrix3 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
print('Дополнительный пример:')
print('входная матрица 3x5:')
for row in matrix3:
    print(row)
print('Результат обхода по спирали:')
print('заканчивается на 9, т.е. выходим на 9.')
print(solution.spiralOrder(matrix3))