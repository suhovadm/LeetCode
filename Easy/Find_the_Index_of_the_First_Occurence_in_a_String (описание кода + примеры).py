# Заводим класс Solution, как того требует LeetCode.
class Solution:

    # Заводим метод strStr, внутри которого:
    # haystack - строка, в которой будем искать.
    # needle - подстрока, которую будем искать.
    # Дальше возвращается либо индекс первого вхождения, либо -1, если ничего не найдено.
    def strStr(self, haystack: str, needle: str) -> int:

        # Обрабатываем пустую строку.
        # Если needle пустая строка, возвращаем 0.
        # Согласно соглашению, пустая строка считается найденной в начале любой строки.
        # not needle тоже самое что len(needle) == 0.
        if not needle:
            return 0

        # Вычисляем длину строк.
        # Каждую длину закидываем в одноимённую перемнную для удобства.
        len_haystack = len(haystack)
        len_needle = len(needle)

        # Запускаем цикл поиска.
        # range(len_haystack - len_needle + 1 - определяет все возможные позиции для поиска.
        # len_haystack - len_needle + 1 - вычисляет максимальный индекс, с которого можно
        # начинать поиск.
        # Например: если haystack = "hello" (длина 5), needle = "ll" (длина 2), то цикл
        # пройдёт по индексам: 0, 1, 2, 3, 4 - (2) = 0, 1, 2, 3
        # Зачем здесь +1?
        # range() в Python создаёт последовательность, которая не включает последнее число.
        # Поэтому добавляем +1, чтобы включить этот последний индекс.
        for i in range(len_haystack - len_needle + 1):

            # Проверка совпадения:
            # haystack[i:i + len_needle] - извлекает подстроку той же длины, что и needle,
            # начиная с позиции i. Здесь используется срез строки.
            # Если извлеченная подстрока равна needle, возвращаем текущий индекс i.
            if haystack[i:i + len_needle] == needle:
                return i

        # Возвращаем -1 если ничего не найдено, как индикатор неудачи.
        # Если цикл завершился без возврата, значит подстрока не найдена.
        return -1

# Примеры.

# Создаём экземпляр класса.
# Инкапсуляция: группируем связанные методы в один объект.
solution = Solution()

# Тест 1: стандартный случай.
print('=' * 50)
print("Тест 1: haystack='hello', needle='ll'")
result = solution.strStr("hello", "ll")
print(f'Результат: {result}') # 2
print('=' * 50)
print()

# Тест 2: подстрока в начале.
print('=' * 50)
print("Тест 2: haystack='hello', needle='he'")
result = solution.strStr("hello", "he")
print(f'Результат: {result}') # 0
print('=' * 50)
print()

# Тест 3: подстройка не найдена.
print('=' * 50)
print("Тест 3: haystack='hello', needle='world'")
result = solution.strStr("hello", "world")
print(f'Результат: {result}') # -1
print('=' * 50)
print()

# Тест 4: пустая подстрока.
print('=' * 50)
print("Тест 4: haystack='hello', needle=''")
result = solution.strStr("hello", "")
print(f'Результат: {result}') # 0
print('=' * 50)
print()

# Тест 5: полное совпадение.
print('=' * 50)
print("Тест 5: haystack='hello', needle='hello'")
result = solution.strStr("hello", "hello")
print(f'Результат: {result}') # 0
print('=' * 50)
print()

# Тест 6: множественные вхождения.
print('=' * 50)
print("Тест 6: haystack='mississippi', needle='iss'")
result = solution.strStr("mississippi", "iss")
print(f'Результат: {result}') # 1 (первое вхождение)
print('=' * 50)
print()

# Тест 7: подстрока длиннее строки.
print('=' * 50)
print("Тест 7: haystack='hi', needle='hello'")
result = solution.strStr("hi", "hello")
print(f'Результат: {result}') # -1
print('=' * 50)

# Пример haystack = "hello", needle = "ll":
# 1. len_haystack = 5, len_needle = 2
# 2. range(5 - 2 + 1) = range(4) -> 0, 1, 2, 3
# 3. Итерации:
# i = 0: haystack[0:2] = "he" != "ll" -> продолжаем.
# i = 1: haystack[1:3] = "el" != "ll" -> продолжаем.
# i = 2: haystack[2:4] = "ll" == "ll" -> возвращаем.
# Этот алгоритм известен как наивный алгоритм поиска подстроки.
# Он прост для понимания, но не самый эффективный для больших строк.
# Для производственного кода обычно используются более эффективные
# Алгоритмы, такие как КМП (Кнута-Морриса-Пратта), Бойера-Мура или алгоритм Рабина-Карпа.
