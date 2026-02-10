from ThreeSumClosest import *

# Запускаем экземпляр класса, выводим результат.
solution = Solution()

# Пример 1.
nums1 = [-1, 2, 1, -4]
target1 = 1
print(f'Пример 1: nums={nums1}, target={target1}')
result1 = solution.threeSumClosest(nums1, target1)
print(f'Результат: {result1}')
print(f'Ожидалось: 2')
print(f'Правильно: {result1 == 2}')

# Пример 2.
nums2 = [0, 0, 0]
target2 = 1
print(f'\nПример 2: nums={nums2}, target={target2}')
result2 = solution.threeSumClosest(nums2, target2)
print(f'Результат: {result2}')
print(f'Ожидалось: 0')
print(f'Правильно: {result2 == 0}')

# Объяснение первого примера.

# Шаг 1.
# nums = [-1, 2, 1, -4]
# target = 1

# Шаг 2. Сортируем массив:
# nums.sort() // результат: [-4, -1, 1, 2]

# Шаг 3. Выводим в closest:
# т.е. берём первые три элемента отсортированного массива: -4, -1, 1 и складываем их.
# closest = nums[0] + nums[1] + nums[2] // -4 + (-1) + 1 = -4

# Шаг 4. Внешний цикл - первая итерация (i = 0)
# nums[i] = nums[0] = -4

# Шаг 4.1. Инициализация указателей.
# left = i + 1 = 1
# right = len(nums) - 1 = 3

# Шаг 4.2. Внутренний цикл.

# Итерация 1:
# left = 1, right = 3
# total = nums[0] + nums[1] + nums[3] = -4 + (-1) + 2 = -3
# total != target (-3 ≠ 1)

# Сравнение отклонений:

# |total - target| = | -3 - 1 | = 4
# |closest - target| = | -4 - 1 | = 5
# 4 < 5, поэтому closest = -3
# total < target (-3 < 1), поэтому left += 1 → left = 2

# Итерация 2:
# left = 2, right = 3
# total = nums[0] + nums[2] + nums[3] = -4 + 1 + 2 = -1
# total != target (-1 ≠ 1)

# Сравнение отклонений:
# |total - target| = | -1 - 1 | = 2
# |closest - target| = | -3 - 1 | = 4
# 2 < 4, поэтому closest = -1
# total < target (-1 < 1), поэтому left += 1 → left = 3
# Условие left < right (3 < 3) ложно --> внутренний цикл завершен.
# Итог после i=0: closest = -1 с отклонением 2

# Шаг 5: Внешний цикл - вторая итерация (i = 1)
# nums[i] = nums[1] = -1

# Шаг 5.1: Инициализация указателей
# left = i + 1 = 2
# right = len(nums) - 1 = 3

# Шаг 5.2: Внутренний цикл

# Итерация 1:
# left = 2, right = 3
# total = nums[1] + nums[2] + nums[3] = -1 + 1 + 2 = 2
# total != target (2 ≠ 1)

# Сравнение отклонений:
# |total - target| = | 2 - 1 | = 1
# |closest - target| = | -1 - 1 | = 2
# 1 < 2, поэтому closest = 2
# total > target (2 > 1), поэтому right -= 1 --> right = 2
# Условие left < right (2 < 2) ложно --> внутренний цикл завершен.
# Итог после i=1: closest = 2 с отклонением 1

# Шаг 6: Завершение внешнего цикла
# i = 2 не выполняется, так как range(len(nums) - 2) = range(2) даёт значения 0 и 1

# Шаг 7: Возврат результата
# return closest  # возвращает 2