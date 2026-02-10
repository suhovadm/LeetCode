from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode() # фиктивный узел для упрощения логики.
        current = dummy     # указатель на последний узел в новом списке.

        # Пока оба списка содержат элементы
        while list1 and list2:
            # выбираем меньший элемент из двух списков.
            if list1.val <= list2.val:
                current.next = list1    # Добавляем list1 в результат
                list1 = list1.next      # Перемещаемся к следующему в list1
            else:
                current.next = list2    # Добавляем list2 в результат
                list2 = list2.next      # Перемещаемся к следующему в list2
            current = current.next      # Перемещаем указатель на последний добавленный.

        # Добавляем оставшиеся элементы, если они есть.
        current.next = list1 if list1 else list2

        return dummy.next # Пропускаем фиктивный узел.

# Вспомогательные функции для тестирования.
def create_linked_list(values):
    # Создаём связный список из списка значений.
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    # Выводим связанный список в виде списка.
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    print(result)

def test_example(example_name, list1_vals, list2_vals):
    # Тестирует и выводит результат для примера.
    print(f"\n{'=' * 50}")
    print(f"Пример: {example_name}")
    print(f"{'=' * 50}")

    # Создаём списки.
    list1 = create_linked_list(list1_vals)
    list2 = create_linked_list(list2_vals)

    print(f"list1: {list1_vals}")
    print(f"list2: {list2_vals}")

    # Объединяем.
    solution = Solution()
    merged = solution.mergeTwoLists(list1, list2)

    # Выводим результат.
    print('Объединённый список:', end=' ')
    print_linked_list(merged)

# Тестируем примеры из условия.
if __name__ == "__main__":

    # Пример 1: [1,2,4] и [1,3,4]
    test_example('Пример 1', [1,2,4], [1,3,4])

    # Пример 2: [] и []
    test_example('Пример 2', [], [])

    # Пример 3: [] и [0]
    test_example('Пример 3', [], [0])

    # Дополнительные примеры.
    test_example('Разные длины', [1,5,9], [2,3,6,10])
    test_example('Один пустой', [1,2,3], [])
    test_example('Дубликаты', [1,1,3], [1,2,2])

    print(f"\n{'=' * 50}")
    print("Объяснение работы алгоритма:")
    print("1. Создаётся фиктивный узел для упрощения логики")
    print("2. Указатель current отслеживает конец нового списка")
    print("3. Пока оба списка не пусты, выбираем меньший элемент")
    print("4. Добавляем выбранный элемент к результату")
    print("5. Когда один список заканчивается, прицепляем остаток другого")
    print("6. Возвращаем результат, пропуская фиктивный узел")
