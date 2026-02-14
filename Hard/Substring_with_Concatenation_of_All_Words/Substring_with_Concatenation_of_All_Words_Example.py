from Substring_with_Concatenation_of_All_Words import *

# Функция для красивого вывода примеров
def print_example(s: str, words: List[str], expected: List[int]):
    print(f"\nПРИМЕР:")
    print(f"  s = '{s}'")
    print(f"  words = {words}")
    print(f"  Ожидаемый результат: {expected}")

    solution = Solution()
    result = solution.findSubstring(s, words)

    print(f"  РЕЗУЛЬТАТ: {result}")
    print(f"  Совпадает с ожидаемым: {'✅ ДА' if sorted(result) == sorted(expected) else '❌ НЕТ'}")
    if result:
        print(f"  Найденные подстроки:")
        word_length = len(words[0]) if words else 0
        total_length = word_length * len(words) if words else 0
        for idx in result:
            print(f"    - индекс {idx}: '{s[idx:idx + total_length]}'")
    print()

if __name__ == "__main__":

    print("-" * 60)
    print("\nПРИМЕР 1: barfoothefoobarman")
    print("Ищем подстроки, которые являются перестановкой слов 'foo' и 'bar' (длина 6)")
    print_example("barfoothefoobarman", ["foo", "bar"], [0, 9])
    print("  Индекс 0: 'barfoo' (bar + foo)")
    print("  Индекс 9: 'foobar' (foo + bar)")

    print("-" * 60)
    print("\nПРИМЕР 2: wordgoodgoodgoodbestword")
    print("Ищем подстроки из 4 слов (общая длина 16), где есть два 'word', одно 'good', одно 'best'")
    print_example("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], [])
    print("  Ничего не найдено, потому что:")
    print("    - 'wordgoodgoodgood' (3 good, нужно 1)")
    print("    - 'goodgoodgoodbest' (нет word)")
    print("    - 'goodgoodbestword' (1 good, нужно 1 good и 2 word)")

    print("-" * 60)
    print("\nПРИМЕР 3: barfoofoobarthefoobarman")
    print("Ищем подстроки из 3 слов (длина 9), перестановки 'bar', 'foo', 'the'")
    print_example("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12])
    print("  Индекс 6: 'foobarthe' (foo + bar + the)")
    print("  Индекс 9: 'barthefoo' (bar + the + foo)")
    print("  Индекс 12: 'thefoobar' (the + foo + bar)")

    print("-" * 60)
    print("\nПРИМЕР 4: Повторяющиеся слова")
    print("Ищем подстроки из двух 'aa' (общая длина 4)")
    print_example("aaaabaaaab", ["aa", "aa"], [0, 5])
    print("  Индекс 0: 'aaaa' ✓")
    print("  Индекс 5: 'aaaa' ✓")
    print("  Пример проверяет корректную работу с повторениями.")

    print("-" * 60)
    print("\nПРИМЕР 5: Пустая строка")
    print("Ищем подстроки в пустой строке")
    print_example("", ["foo", "bar"], [])
    print("  Результат: [] (очевидно)")

    print("-" * 60)
    print("\nПРИМЕР 6: Одно слово")
    print("Ищем подстроки из одного слова 'foo' (длина 3)")
    print_example("foobar", ["foo"], [0])
    print("  Индекс 0: 'foo'")

    print("-" * 60)
    print("\nПРИМЕР 7: Все слова одинаковые")
    print("Ищем подстроки из трех 'aa' (длина 6)")
    print_example("aaaaaa", ["aa", "aa", "aa"], [0])
    print("  Индекс 0: 'aaaaaa' (aa + aa + aa)")

    print("-" * 60)
    print("\nПРИМЕР 8: Сложный случай")
    print("Ищем подстроку длиной 20, содержащую: 'fooo' (1), 'barr' (1), 'wing' (2), 'ding' (1)")
    print_example("lingmindraboofooowingdingbarrwingmonkeypoundcake",
                  ["fooo", "barr", "wing", "ding", "wing"],
                  [13])
    print("  Индекс 13: разбираем по словам (длина каждого 4):")
    print("    13-16: 'fooo' ✓")
    print("    17-20: 'wing' ✓ (первый wing)")
    print("    21-24: 'ding' ✓")
    print("    25-28: 'barr' ✓")
    print("    29-32: 'wing' ✓ (второй wing)")
    print("    Итого: 'foooowingdingbarrwing' (fooo + wing + ding + barr + wing)")
    print("-" * 60)