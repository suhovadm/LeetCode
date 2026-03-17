from Valid_Palindrome import *

# Создаём экземпляр класса Solution.
solution = Solution()

# Пример 1.
s1 = "A man, a plan, a canal: Panama"
result1 = solution.isPalindrome(s1)
print(f'Вход: s = "{s1}"')
print(f'Выход: {result1}')
print(f'Объяснение: "amanaplanacanalpanama" — это палиндром.')
print()

# Пример 2.
s2 = "race a car"
result2 = solution.isPalindrome(s2)
print(f'Вход: s = "{s2}"')
print(f'Выхд: {result2}')
print(f'Объяснение: "raceacar" не является палиндромом.')
print()

# Пример 3.
s3 = " "
result3 = solution.isPalindrome(s3)
print(f'Вход: s = "{s3}"')
print(f'Выход: {result3}')
print(f'Объяснение: После удаления неалфавитно-цифровых символов строка s становится пустой строкой "".')
print(f'Поскольку пустая строка читается одинаково слева направо и справа налево, она является палиндромом.')