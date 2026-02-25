from Remove_Nth_Node_From_End_of_List import *

# Вывод примера в консоль.

# Заводим функцию print_list, которая принимает 1 параметр - head.
# head - указатель на первый узел связного списка.
def print_list(head):

    # Создаём пустой список values, который будет хранить строковые
    # значения всех узлов списка.
    values = []
    # Указатель на начло. Создаём переменную current, которая указывает на голову списка.
    # Эта переменная будет использоваться для прохода по всем узлам.
    current = head

    # Запускаем цикл while, который будет выполняться до тех пор, пока current
    # не станет None (пока не достигнем конца списка).
    while current:
        # На каждой итерации значение текущего узла (current.val) преобразуется в строку
        # с помощью str() и добавляется в конец списка values методом append().
        values.append(str(current.val))
        # Переходим к следующему узлу. Указатель current перемещается на следующий узел списка.
        # Если текущий узел был последним, current.next вернёт None, и цикл завершится на следующей
        # проверке.
        current = current.next

    # Вывод результата.
    # Если список values не пустой (есть хотя бы один узел), то метод join() объединяет все
    # элементы списка в строку, вставляя между ними стрелочку.
    # Если список пустой (нет узлов), выводится "[]".
    print(" -> ".join(values) if values else "[]")

head = ListNode(1) # <-- 5
head.next = ListNode(2) # <-- 4
head.next.next = ListNode(3) # <-- 3
head.next.next.next = ListNode(4) # <-- наш n = 2, который мы удаляем!
head.next.next.next.next = ListNode(5) # <-- 1

print("Исходный список:")
print_list(head)

n = 2
solution = Solution()
result = solution.removeNthFromEnd(head, n)

print(f'\nПосле удаления {n}-го узла с конца:')
print_list(result)

# Пример работы:
# Для списка [1,2,3,4,5] и n = 2:
# Создаем dummy(0) -> 1 -> 2 -> 3 -> 4 -> 5
# fast и slow указывают на dummy
# Сдвигаем fast на 3 позиции: fast указывает на 3
# Двигаем оба указателя, пока fast не станет None:
# fast переходит с 3 на 4, slow с dummy на 1
# fast переходит с 4 на 5, slow с 1 на 2
# fast переходит с 5 на None, slow с 2 на 3
# slow указывает на 3, удаляемый узел - 4
# slow.next = slow.next.next перенаправляет 3.next с 4 на 5
# Возвращаем dummy.next (узел 1), получаем [1,2,3,5]