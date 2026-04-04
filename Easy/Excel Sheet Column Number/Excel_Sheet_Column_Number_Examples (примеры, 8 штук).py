from Excel_Sheet_Column_Number import Solution

# Примеры работы.

# Пример 1: 'AB'
# 1. result = 0
# char = 'A'
# цифра = ord('A')-65+1 = 1
# result = 0*26 + 1 = 1

# 2. char = 'B'
# цифра = ord('B')-65+1 = 2
# result = 1*26 + 2 = 28
# Результат: 28 (что соответствует Excel: A=1, B=2 - AB=28)

# Пример 2: "zz"
# 1. result = 0
# 'Z' - цифра = 26
# result = 0*26 + 26 = 26
# 2. 'Z' - цифра = 26
# result = 26*26 + 26 = 676 + 26 = 702
# Результат: 702

# Пример 3: "FXSHRXW" (максимальное в старой версии Excel)
# Код просто пройдёт по всем символам слева направо, каждый раз умножая результат
# на 26 и прибавляя цифру текущей буквы. Это работает для любой длины.

# -----------------------------------------------------------------------------------

# Вывод в консоль:

# Создаём экземпляр класса.
solution = Solution()

# Пример 1: одна буква A.
print(f'"{"A"}" -> {solution.titleToNumber("A")}') # 1

# Пример 2: одна буква Z.
print(f'"{"Z"}" -> {solution.titleToNumber("Z")}') # 26

# Пример 3: две буквы AB.
print(f'"{"AB"}" -> {solution.titleToNumber("AB")}') # 28

# Пример 4: две буквы ZZ.
print(f'"{"ZZ"}" -> {solution.titleToNumber("ZZ")}') # 702

# Пример 5: три буквы ABC.
print(f'"{"ABC"}" -> {solution.titleToNumber("ABC")}') # 731

# Пример 6: три буквы AAA.
print(f'"{"AAA"}" -> {solution.titleToNumber("AAA")}') # 703

# Пример 7: сложный пример из условия.
print(f'"{ "FXSHRXW" }" -> {solution.titleToNumber("FXSHRXW")}') # 2147483647

# Пример 8: слово CODE.
print(f'"{ "CODE" }" -> {solution.titleToNumber("CODE")}') # 62977