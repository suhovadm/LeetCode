# Combination Sum II

# Дан набор чисел-кандидатов (candidates) и целевое число (target).
# Найдите все уникальные комбинации из candidates, в которых сумма чисел равна target.

# Каждое число из candidates может быть использовано в комбинации только один раз.

# Примечание: результирующий набор не должен содержать повторяющихся комбинаций.

# Пример 1:
# Входные данные: candidates = [10,1,2,7,6,1,5], target = 8

# Результат:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

# Пример 2:
# Входные данные: candidates = [2,5,2,1,2], target = 5
# Результат:
# [
# [1,2,2],
# [5]
# ]

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        result = []

        def backtrack(remaining_target: int, start: int, current_combination: List[int]):

            if remaining_target == 0:
                result.append(current_combination.copy())
                return

            if remaining_target < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining_target:
                    break

                current_combination.append(candidates[i])

                backtrack(remaining_target - candidates[i], i + 1, current_combination)

                current_combination.pop()

        backtrack(target, 0, [])
        return result

# Как работает алгоритм?
# 1. Сортировка - сортируем массив, чтобы легко обрабатывать дубликаты.

# 2. Уникальность комбинаций - пропускаем дубликаты с помощью условия:
# i > start and candidates[i] == candidates[i - 1]

# 3. Оптимизация - если текущий элемент больше оставшейся суммы, прекращаем итерацию (break).

# 4. Каждый элемент используется только один раз - при рекурсивном вызове передаём i + 1.

# 5. Backtracking - после рекурсивного вызова удаляем последний элемент из комбинации.

# Сложность:
# время: O(2^n) в худшем случае, но с отсечениями работает быстрее,
# память: O(n) для хранения текущей комбинации.