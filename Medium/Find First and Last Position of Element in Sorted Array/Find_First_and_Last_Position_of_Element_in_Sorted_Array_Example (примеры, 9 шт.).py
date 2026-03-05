from Find_First_and_Last_Position_of_Element_in_Sorted_Array import *

# Создаём экземпляр класса для тестирования.
solution = Solution()

# Пример 1: target найден в середине массива.
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
result1 = solution.searchRange(nums1, target1)
print(f'Пример 1: nums = {nums1}, target = {target1}')
print(f'Результат: {result1}')
print(f'Объяснение: число {target1} встречается на позициях {result1[0]} и {result1[1]}')
print()

# Пример 2: target не найден.
nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
result2 = solution.searchRange(nums2, target2)
print(f'Пример 2: nums = {nums2}, target = {target2}')
print(f'Результат: {result2}')
print(f'Объяснение: число {result2} отсутствует в массиве.')
print()

# Пример 3: пустой массив.
nums3 = []
target3 = 0
result3 = solution.searchRange(nums3, target3)
print(f'Пример 3: nums = {nums3}, target = {target3}')
print(f'Результат: {result3}')
print(f'Объяснение: массив пуст.')
print()

# Пример 4: target в начале массива.
nums4 = [2, 2, 2, 3, 4, 5]
target4 = 2
result4 = solution.searchRange(nums4, target4)
print(f'Пример 4: nums = {nums4}, target = {target4}')
print(f'Результат: {result4}')
print(f'Объяснение: число {target4} встречается с позиции {result4[0]} по {result4[1]}')
print()

# Пример 5: target в конце массива.
nums5 = [1, 2, 3, 4, 5, 5, 5]
target5 = 5
result5 = solution.searchRange(nums5, target5)
print(f'Пример 5: nums = {nums5}, target = {target5}')
print(f'Результат: {result5}')
print(f'Объяснение: число {target5} встречается с позиции {result5[0]} по {result5[1]}')
print()

# Пример 6: весь массив состоит из одного числа.
nums6 = [7, 7, 7, 7, 7]
target6 = 7
result6 = solution.searchRange(nums6, target6)
print(f'Пример 6: nums = {nums6}, target = {target6}')
print(f'Результат: {result6}')
print(f'Объяснение: весь массив состоит из числа {target6}')
print()

# Пример 7: массив из одного элемента.
nums7 = [42]
target7 = 42
result7 = solution.searchRange(nums7, target7)
print(f'Пример 7: nums = {nums7}, target = {target7}')
print(f'Результат: {result7}')
print(f'Объяснение: единственный элемент массива равен target.')
print()

# Пример 8: target больше всех элементов.
nums8 = [1, 2, 3, 4, 5]
target8 = 10
result8 = solution.searchRange(nums8, target8)
print(f'Пример 8: nums = {nums8}, target = {target8}')
print(f'Результат: {result8}')
print(f'Объяснение: target больше всех элементов массива.')
print()

# Пример 9: target меньше всех элементов.
nums9 = [10, 20, 30, 40, 50]
target9 = 5
result9 = solution.searchRange(nums9, target9)
print(f'Пример 9: nums {nums9}, target = {target9}')
print(f'Результат: {result9}')
print(f'Объяснение: target меньше всех элементов массива.')