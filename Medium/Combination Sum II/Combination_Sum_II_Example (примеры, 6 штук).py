from Combination_Sum_II import *

# Пример работы для candidates = [1,1,2,5,6,7,10], target = 8:
# 1. Сортируем [1,1,2,5,6,7,10]
# 2. Начинаем с первой 1: ищем комбинацию с суммой 7
# 3. Находим [1,1,6], [1,2,5], [1,7] // из каждой комбо можно получить 8
# 4. Пропускаем вторую 1 на верхнем уровне (continue)
# 5. Начинаем с 2: находим [2,6] // здесь тоже можно получить 8
# 6. Начинаем с 5: 5 + 7 > 8, поэтому break // здесь уже нельзя получить 8, поэтому break
# 7. Возвращаем все найденные комбинации.

# Пример 1.
print("Пример 1:")
print("Входные данные: candidates = [10,1,2,7,6,1,5], target = 8")
solution = Solution()
result1 = solution.combinationSum2([10,1,2,7,6,1,5], 8)
print("Результат:", result1)
print()

# Пример 2.
print("Пример 2:")
print("Входные данные: candidates = [2,5,2,1,2], target = 5")
result2 = solution.combinationSum2([2,5,2,1,2], 5)
print("Результат:", result2)
print()

# Дополнительные примеры.
print("Дополнительные примеры:")

# Пример 3: Пустой массив.
print("\nПример 3 (пустой массив):")
print("Входные данные: candidates = [], target = 5")
result3 = solution.combinationSum2([], 5)
print("Результат:", result3)

# Пример 4: Одно число.
print("\nПример 4 (одно число):")
print("Входные данные: candidates = [5], target = 5")
result4 = solution.combinationSum2([5], 5)
print("Результат:", result4)

# Пример 5: Невозможная комбинация.
print("\nПример 5 (невозможная комбинация):")
print("Входные данные: candidates = [2,4,6], target = 5")
result5 = solution.combinationSum2([2,4,6], 5)
print("Результат:", result5)

# Пример 6: Много дубликатов.
print("\nПример 6 (много дубликатов):")
print("Входные данные: candidates = [1,1,1,1,1,1,1], target = 3")
result6 = solution.combinationSum2([1,1,1,1,1,1,1], 3)
print("Результат:", result6)