from Longest_Valid_Parentheses import *

# Примеры использования:
solution = Solution()

# Пример 1.
s1 = "(()"
result1 = solution.longestValidParentheses(s1)
print(f"Пример 1: s = \"{s1}\"")
print(f"Результат: {result1}")
print(f"Пояснение: самая длинная допустимая подстрока скобок это \"{'()' if result1 == 2 else s1}\"")
print()

# Пример 2.
s2 = ")()())"
result2 = solution.longestValidParentheses(s2)
print(f"Пример 2: s = \"{s2}\"")
print(f"Результат: {result2}")
print(f"Пояснение: самая длинная допустимая подстрока скобок это \"{'()()' if result2 == 4 else s2}\"")
print()

# Пример 3.
s3 = ""
result3 = solution.longestValidParentheses(s3)
print(f"Пример 3: s = \"{s3}\"")
print(f"Результат: {result3}")
print(f"Пояснение: {'' if result3 == 0 else 'неправильно'}")
print()

# Дополнительные примеры.
test_strings = [
    "()", # Классическая пара, длина 2.
    "()(())", # Длина 6.
    "(()())", # Здесь одна непрерывная последовательность, т.е. скобки в скобках. Длина 6.
    "((()))", # Здесь простая вложенная структура, все скобки закрываются в правильном порядке. Длина 6.
    "()(()", # Индексы 0-1: валидно, длина 2. Индексы 2-4: невалидно. Индексы 3-4: валидно, длина 2. Вся строка: невалидно.
    "((()))())" # От 0 до 5 = 6 и от 6 до 7 = 2. 6 + 2 = 8. Одна лишняя (последняя).
]

print("Дополнительные примеры:")
for test in test_strings:
    result = solution.longestValidParentheses(test)
    print(f" s = \"{test}\" -> {result}")