# Даны начала двух отсортированных связанных списков list1 и list2.
# Объедините два списка в один отсортированный список. Список должен быть создан путём
# объединения узлов первых двух списков.

# Верните начало объединённого связанного списка.

# Пример 1:
# Ввод: list1 = [1,2,4], list2 = [1,3,4]
# Вывод: [1,1,2,3,4,4]

# Пример 2:
# Ввод: lis1 = [], list2 = []
# Вывод: []

# Пример 3:
# Ввод: list1 = [], list2 = [0]
# Вывод: [0]

# Ограничения.
# Количество узлов в обоих списках находится в диапазоне [0, 50].
# -100 <= Node.val <= 100
# Оба списка list1 и list2 отсортированы в неубывающем порядке.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2

        return dummy.next

# Как это работает?
# Создаём dummy (фиктивный) узел - это удобный приём, чтобы не обрабатывать отдельно
# случай с пустым списком.
# Переменная current всегда указывает на последний узел в новом списке.
# Сравниваем значения текущих узлов list1 и list2, добавляем меньший к результату.
# Когда один список заканчивается, просто прицепляем остаток другого списка.
# Возвращаем dummy.next - первый реальный узел объединённого списка.
