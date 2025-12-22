# Даны две строки: needle (иголка) b haystack (стог сена).
# Верните индекс первого вхождения строки needle в строку haystack, или -1,
# если needle не является частью haystack.

# Пример 1:
# Ввод: haystack = "sadbutsad", needle = "sad"
# Вывод: 0
# Пояснение: "sad" встречается в индексах 0 и 6.
# Первое вхождение - в индексе 0, поэтому возвращаем 0.

# Пример 2:
# Ввод: haystack = "leetcode", needle = "leeto"
# Вывод: -1
# Пояснение: "leeto" не встречается в "leetcode", поэтому возвращаем -1.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return 0

        len_haystack = len(haystack)
        len_needle = len(needle)

        for i in range(len_haystack - len_needle + 1):
            if haystack[i:i + len_needle] == needle:
                return i

        return -1

# Объяснение.
# 1. Если needle пустая строка - возвращаем 0 (по соглашению).
# 2. Вычислаем длины строк.
# 3. Проходим по haystack, но только до того индекса, где needle ещё может поместиться.
# 4. На каждом шаге сравниваем подстроку haystack с needle.
# 5. Если нашли совпадение - возвращаем индекс.
# 6. Если прошли весь цикл и не нашли - возвращаем -1.

# Существует ещё один вариант с .find(), он самый простой и использует встроенную оптимизацию Python.
# Выглядит он вот так:

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         return haystack.find(needle)

# Данный же вариант показывает, как работает алгоритм "под капотом".
