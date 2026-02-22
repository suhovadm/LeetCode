from swap_nodes_in_pairs import *

# 1. Вспомогательная функция для создания списка из массива.

# Заводим функцию с именем create_linked_list, которая принимает один параметр - arr, т.е.
# массив, т.е. список значений, из которого нужно создать связный список.
def create_linked_list(arr):

    # Проверяем, пустой ли массив arr. Если arr пуст (например, []), то условие
    # if not arr становится истинным.
    # Если массив пуст, функция возвращает None, что означает пустой связный список.
    if not arr:
        return None

    # Создаёт первый узел связного списка.
    # Создаёт новый список, значением которого становится первый элемент массива arr[0]
    head = ListNode(arr[0])
    # head - переменная, хранящая ссылку на этот первый узел (голову списка).
    # current = head - создаёт указатель current, который изначально указывает на голову списка.
    # Этот указатель будет использоваться для добавления новых узлов в конец списка.
    current = head

    # Запускаем цикл for по всем элементам массива, начиная со второго элемента (индекс 1):
    # arr[1:] - это срез массива от второго элемента до конца.
    # val - текущее значение из массива на каждой итерации цикла.
    for val in arr[1:]:
        # Создаём новый узел со значением val и присоединяем его к текущему узлу:
        # ListNode(val) - создаёт новый узел.
        # current.next = ... - устанавливает связь: следующий за текущим узлом - это новый узел.
        current.next = ListNode(val)
        # Перемещаем указатель current на только что созданный узел, чтобы в следующей итерации
        # добавлять новый узел уже после него.
        current = current.next

    # После завершения цикла возвращаем голову созданного связного списка.
    return head

# 2. Вспомогательная функция для вывода списка.

# Создаём функцию print_linked_list(head), которая принимает один параметр head - голову
# связного списка, который нужно вывести.
def print_linked_list(head):

    # Создаём пустой список result, в который будут добавляться значения узлов
    # для последующего вывода.
    result = []
    # Создаём указатель current, который изначально указыват на голову списка.
    # Этот указатель будет использоваться для прохода по всем узлам.
    current = head

    # Запускаем цикл, который выполняется до тех пор, пока current не станет None
    # (то есть пока не будет достигнут конец списка).
    while current:
        # Добавляет значение текущего узла (current.val) в список result.
        result.append(current.val)
        # Перемещает указатель current на следующий узел списка.
        current = current.next
    # После завершения цикла выводит список в консоль. Это даёт удобное визуальное
    # представление связного списка в виде массива Python.
    print(result)

print()

# Пример 1: head = [1, 2, 3, 4]
print('Пример 1:')
head1 = create_linked_list([1, 2, 3, 4])
print('Вход:', end=" ")
print_linked_list(head1)
solution = Solution()
result1 = solution.swapPairs(head1)
print('Выход:', end=" ")
print_linked_list(result1)
print()

# Пример 2: head = []
print('Пример 2:')
head2 = create_linked_list([])
print('Вход:', end=" ")
print_linked_list(head2)
result2 = solution.swapPairs(head2)
print('Выход:', end=" ")
print_linked_list(result2)
print()

# Пример 3: head = [1]
print('Пример 3:')
head3 = create_linked_list([1])
print('Вход:', end=" ")
print_linked_list(head3)
result3 = solution.swapPairs(head3)
print('Выход:', end=" ")
print_linked_list(result3)
print()

# Пример 4: head = [1, 2, 3]
print('Пример 4:')
head4 = create_linked_list([1, 2, 3])
print('Вход:', end=" ")
print_linked_list(head4)
result4 = solution.swapPairs(head4)
print('Выход:', end=" ")
print_linked_list(result4)
print()

# Дополнительный пример: head = [1, 2, 3, 4, 5] (нечётное количество узлов)
print('Дополнительный пример (нечётное количество узлов):')
head5 = create_linked_list([1, 2, 3, 4, 5])
print('Вход:', end=" ")
print_linked_list(head5)
result5= solution.swapPairs(head5)
print('Выход:', end=" ")
print_linked_list(result5)