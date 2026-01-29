# Пример. Цепляемся к основному скрипту и выводим результат на экран в виде таблицы.
from BestTimetoBuyandSellStock import Solution

# ^5 означает: "отформатируй это значение, сделав ширину поля 5 символов и выровняй по центру."
# :>5 - выравнивание по правому краю
# :<5 - выравнивание по левому краю
# :^5 - выравнивание по центру

def run_example():
    solution = Solution()
    print("Пример выполнения для prices = [7, 1, 5, 3, 6, 4]:")
    print()

    # Входные данные.
    prices = [7, 1, 5, 3, 6, 4]

    # Имитируем работу алгоритма с подробным выводом.
    print(f"{'День':^5} | {'Цена':^6} | {'min_price':^10} | {'current_profit':^15} | {'max_profit':^10} | {'Объяснение':^30}")
    print("-" * 100)

    # Инициализация.
    min_price = prices[0]
    max_profit = 0
    print(f"{0:^5} | {prices[0]:^6} | {min_price:^10} | {'-':^15} | {max_profit:^10} | {'Инициализация':30}")

    # Проходимся по дням.
    for day in range(1, len(prices)):
        current_price = prices[day]

        if current_price < min_price:
            print(f"{day:^5} | {current_price:^6} | {min_price:^10} | {'-':^15} | {max_profit:^10} | {'Цена ниже min_price, обновляем минимум':30}")
            min_price = current_price
        else:
            current_profit = current_price - min_price
            if current_profit > max_profit:
                print(f"{day:^5} | {current_price:^6} | {min_price:^10} | {current_profit:^15} | {max_profit:^10} | {'Прибыль, обновляем максимум':30}")
                max_profit = current_profit
            else:
                print(f"{day:^5} | {current_price:^6} | {min_price:^10} | {current_profit:^15} | {max_profit:^10} | {'Прибыль меньше максимума':30}")

    print("-" * 100)
    print(f"Итог: максимальная прибыль {max_profit}")

    # Вызов функции.
    result = solution.maxProfit(prices)
    print(f"\nФактический результат функции: {result}")
    print(f"Совпадает с ожидаемым результатом: {'Да' if result == 5 else 'Нет'}")

# Точка входа в программу, запуск и вывод на экран.
if __name__ == "__main__":
    run_example()