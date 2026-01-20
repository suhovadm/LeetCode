from Merge_k_Sorted_Lists import *

# ----------------------------------------------------------------------------- #
# Примеры.

def list_to_linkedlist(lst):
    # Преобразуем список в связный список:
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linkedlist_to_list(head):
    # Преобразуем связный список в обычный список.
    result = []
    while head:
        result.append(head.val)
        while head:
            result.append(head.val)
            head = head.next
        return result

# Пример 1: [[1,4,5],[1,3,4],[2,6]]
print('Пример 1:')
# Создаём 3 связных списка.
list1 = list_to_linkedlist([1, 4, 5])
list2 = list_to_linkedlist([1, 3, 4])
list3 = list_to_linkedlist([2, 6])

solution = Solution()
result1 = solution.mergeKLists([list1, list2, list3]) # Передаём список списков.
print('Вход: [[1,4,5],[1,3,4],[2,6]]')
print('Выход:', linkedlist_to_list(result1)) # [1,1,2,3,4,4,5,6]

# Пример 2: [] (пустой список списков)
print('\nПример 2:')
result2 = solution.mergeKLists([]) # Передаём пустой список.
print('Вход: []')
print('Выход:', linkedlist_to_list(result2) if result2 else []) # []

# Пример 3: [[]] (список с одним пустым списком)
print('\nПример 3:')
result3 = solution.mergeKLists([None]) # Передаём список с None.
print('Вход: [[]]')
print('Выход:', linkedlist_to_list(result3) if result3 else []) # []

# Пример 4: [[-2,0,4],[-1,5,10],[3,7,9]]
print('\nПример 4:')
list4 = list_to_linkedlist([-2, 0, 4])
list5 = list_to_linkedlist([-1, 5, 10])
list6 = list_to_linkedlist([3, 7, 9])

result4 = solution.mergeKLists([list4, list5, list6]) # Передаём список списков.
print('Вход: [[-2,0,4],[-1,5,10],[3,7,9]]')
print('Выход:', linkedlist_to_list(result4)) # [-2,-1,0,3,4,5,7,9,10]

# Пример 5: один список.
print('\nПример 5:')
list7 = list_to_linkedlist([1, 2, 3])
result5 = solution.mergeKLists([list7]) # <--- Передаём список с одним элементом, иначе получим ошибку.
print('Вход: [[1,2,3]]')
print('Выход:', linkedlist_to_list(result5)) # [1,2,3]

# Ключевой момент mergeKList принимает список связных списков, поэтому всегда нужно
# передавать список, даже если там всего один элемент.