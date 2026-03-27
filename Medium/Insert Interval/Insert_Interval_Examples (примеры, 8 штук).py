from Insert_Interval import *

# Пример 1: Вставка в середину с пересечением
print("Пример 1:")
intervals1 = [[1, 3], [6, 9]]
newInterval1 = [2, 5]
solution = Solution()
result1 = solution.insert(intervals1, newInterval1)
print(f"Входные интервалы: {intervals1}")
print(f"Новый интервал: {newInterval1}")
print(f"Результат: {result1}")
print()

# Пример 2: Вставка в начало без пересечения
print("Пример 2:")
intervals2 = [[3, 5], [7, 9]]
newInterval2 = [1, 2]
solution = Solution()
result2 = solution.insert(intervals2, newInterval2)
print(f"Входные интервалы: {intervals2}")
print(f"Новый интервал: {newInterval2}")
print(f"Результат: {result2}")
print()

# Пример 3: Вставка в конец без пересечения
print("Пример 3:")
intervals3 = [[1, 2], [3, 4]]
newInterval3 = [5, 6]
solution = Solution()
result3 = solution.insert(intervals3, newInterval3)
print(f"Входные интервалы: {intervals3}")
print(f"Новый интервал: {newInterval3}")
print(f"Результат: {result3}")
print()

# Пример 4: Объединение нескольких интервалов
print("Пример 4:")
intervals4 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval4 = [4, 8]
solution = Solution()
result4 = solution.insert(intervals4, newInterval4)
print(f"Входные интервалы: {intervals4}")
print(f"Новый интервал: {newInterval4}")
print(f"Результат: {result4}")
print()

# Пример 5: Пустой список интервалов
print("Пример 5:")
intervals5 = []
newInterval5 = [5, 7]
solution = Solution()
result5 = solution.insert(intervals5, newInterval5)
print(f"Входные интервалы: {intervals5}")
print(f"Новый интервал: {newInterval5}")
print(f"Результат: {result5}")
print()

# Пример 6: Новый интервал охватывает все существующие
print("Пример 6:")
intervals6 = [[1, 3], [4, 6], [8, 10]]
newInterval6 = [2, 9]
solution = Solution()
result6 = solution.insert(intervals6, newInterval6)
print(f"Входные интервалы: {intervals6}")
print(f"Новый интервал: {newInterval6}")
print(f"Результат: {result6}")
print()

# Пример 7: Касание интервалов (граничные условия)
print("Пример 7:")
intervals7 = [[1, 3], [6, 9]]
newInterval7 = [3, 6]
solution = Solution()
result7 = solution.insert(intervals7, newInterval7)
print(f"Входные интервалы: {intervals7}")
print(f"Новый интервал: {newInterval7}")
print(f"Результат: {result7}")
print()

# Пример 8: Вставка между интервалами без пересечения
print("Пример 8:")
intervals8 = [[1, 2], [7, 8]]
newInterval8 = [4, 5]
solution = Solution()
result8 = solution.insert(intervals8, newInterval8)
print(f"Входные интервалы: {intervals8}")
print(f"Новый интервал: {newInterval8}")
print(f"Результат: {result8}")