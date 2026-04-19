from Linked_List_Cycle import *

# Точка входа в программу.
if __name__ == '__main__':

    # Создаём экземпляр класса.
    sol = Solution()

    # Пример 1: head = [3,2,0,-4], pos = 1 (цикл, хвост указывает на узел с индексом 1).
    # Строим узлы.
    node0 = ListNode(3)
    node1 = ListNode(2) # <--- указывает сюда!
    node2 = ListNode(0)
    node3 = ListNode(-4)

    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node1  # pos = 1 -> последний указывает на узел со значением 2.

    print('Пример 1: head = [3,2,0,-4], pos = 1')
    print('Результат:', sol.hasCycle(node0))  # ожидается [True].
    print()

    # Пример 2: head = [1,2], pos = 0 (цикл, хвост указывает на первый узел).
    n0 = ListNode(1) # <--- указывает сюда!
    n1 = ListNode(2)
    n0.next = n1
    n1.next = n0  # pos = 0 -> последний указывает на узел со значением 1.

    print('Пример 2: head = [1,2], pos = 0')
    print('Результат:', sol.hasCycle(n0))  # ожидается [True].
    print()

    # Пример 3: head = [1], pos = -1 (нет цикла).
    m0 = ListNode(1)
    # m0.next остаётся None. Цикла нет!

    print('Пример 3: head = [1], pos = -1')
    print('Результат:', sol.hasCycle(m0))  # ожидается [False].