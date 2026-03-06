# Check if Binary String Has at Most One Segment of Ones

# Учитывая двоичную строку s без ведущих нулей, верните true, если s содержит
# не более одного непрерывного сегмента едениц. В противном случае верните False.

# Пример 1:
# Вход: s "1001"
# Выход: false
# Объяснение: еденицы не образуют непрерывный сегмент.

# Пример 2:
# Вход: s = "110"
# Выход: true

# Ограничения:
# 1 <= s.length <= 100
# s[i] - это либо '0', либо '1'.
# s[0] равен '1'.

class Solution:
    def checkOnesSegment(self, s: str) -> bool:

        return "01" not in s

# Объяснение алгоритма:
# поскольку строка начинается с '1' (по условию), то:
# если в строке есть подстрока "01", это означает, что после непрерывного сегмента
# едениц идёт ноль, а затем где-то дальше снова еденица.
# Это как раз и означает наличие двух отдельных сегментов едениц.
# Если "01" не найден, значит либо все еденицы идут подряд до конца строки, либо
# после едениц идут только нули.

# Сложность:
# время: O(n), где n - длина строки,
# память: O(1).

def test_algorithm():
    solution = Solution()

    # Тестовые примеры.
    test_cases = [
        "1001",
        "110",
        "1",
        "101",
        "111",
        "1100",
        "1010",
        "1000",
        "111001",
        "10"
    ]

    print("=" * 50)
    print("ТЕСТИРОВАНИЕ АЛГОРИТМА")
    print("=" * 50)

    for s in test_cases:
        result = solution.checkOnesSegment(s)
        print(f"Входная строка: '{s}'")
        print(f"Результат: {result}")
        print(f"Объяснение: {'Один непрерывный сегмент' if result else 'Более одного сегмента'}")

        # Визуализация сегментов.
        if result:
            print(f"Сегменты единиц: [один непрерывный сегмент]")
        else:
            # Находим все сегменты единиц для наглядности.
            segments = []
            in_segment = False
            start = 0

            for i, char in enumerate(s):
                if char == '1' and not in_segment:
                    in_segment = True
                    start = i
                elif char == '0' and in_segment:
                    in_segment = False
                    segments.append(f"с {start} по {i - 1}")

            if in_segment:
                segments.append(f"с {start} по {len(s) - 1}")

            print(f"Сегменты единиц: {', '.join(segments)}")

        print("-" * 50)

    print("\nДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ:")
    print("-" * 50)

    # Граничные случаи
    edge_cases = [
        "1" * 100,  # 100 единиц
        "1" * 50 + "0" * 50,  # 50 единиц, потом 50 нулей
        "10" * 50,  # чередование 1 и 0
    ]

    for i, s in enumerate(edge_cases):
        if len(s) > 20:  # Для длинных строк показываем только начало
            display_s = s[:20] + "..."
        else:
            display_s = s

        result = solution.checkOnesSegment(s)
        print(f"Строка {i + 1}: '{display_s}' (длина: {len(s)})")
        print(f"Результат: {result}")
        print(f"→ {'Один сегмент' if result else 'Несколько сегментов'}")
        print("-" * 30)

# Запускаем всё это добро.
if __name__ == "__main__":
    test_algorithm()