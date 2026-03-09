# Импортируем тип Optional из модуля типизации.
# Optional[TreeNode] означает "либо TreeNode, либо None".
from typing import Optional

# Заводим класс TreeNode. Это класс узла бинарного дерева.
# val - значение узла, по умолчанию 0.
# left - левый потомок, по умолчанию None.
# right - правый потомок, по умолчанию None.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Заводим класс Solution с методом isSame Tree.
class Solution:
    # Метод isSameTree принимает два параметра - это корни деревьев p и q.
    # Каждый может быть TreeNode или None.
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Основная логика метода:

        # Базовый случай рекурсии: если оба узла p и q равны None (пустые),
        # значит мы дошли до конца ветки в обоих деревьях одновременно - возвращаем True.
        if not p and not q:
            return True

        # Если только один из узлов пустой, а другой нет - структуры деревьев разные.
        # Например:
        # p имеет левого потомка, а q в этой позиции None.
        # p = None, а q содержит узел.
        if not p or not q:
            return False

        # Если значения в текущих узлах разные - деревья не идентичны. Например:
        # В p узел со значением 5.
        # В q узел со значением 3.
        if p.val != q.val:
            return False

        # Рекурсивный вызов:
        # self.isSameTree(p.left, q.left) - проверяем, идентичны ли левые поддеревья.
        # self.isSameTree(p.right, q.right) - проверяем, идентичны ли правые поддеревья.
        # and - оба должны быть True для того, чтобы всё дерево было одинаковым.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# ----- Пример 1: [1,2,3] и [1,2,3] -----
print('Пример 1: одинаковые деревья [1,2,3]')
# Создаем дерево p: [1,2,3]
#     1
#    / \
#   2   3
p1 = TreeNode(1)
p1.left = TreeNode(2)
p1.right = TreeNode(3)

# Создаём дерево q: [1,2,3]
#     1
#    / \
#   2   3
q1 = TreeNode(1)
q1.left = TreeNode(2)
q1.right = TreeNode(3)

solution = Solution()
result1 = solution.isSameTree(p1, q1)
print(f'Дерево p = [1,2,3], дерево q = [1,2,3]')
print(f'Результат: {result1}\n') # True

# ----- Пример 2: [1,2] и [1,null,2] -----
print('Пример 2: разные структуры [1,2] и [1,null,2]')
# Создаем дерево p: [1,2]
#     1
#    /
#   2
p2 = TreeNode(1)
p2.left = TreeNode(2)

# Создаем дерево q: [1,null,2]
#     1
#      \
#       2
q2 = TreeNode(1)
q2.right = TreeNode(2)

result2 = solution.isSameTree(p2, q2)
print(f'Дерево p = [1,2], дерево q = [1,null,2]')
print(f'Результат: {result2}\n') # False

# ----- Пример 3: [1,2,1] и [1,1,2] -----
print('Пример 3: одинаковые структуры, но разные значения [1,2,1] и [1,1,2]')
# Создаем дерево p: [1,2,1]
#     1
#    / \
#   2   1
p3 = TreeNode(1)
p3.left = TreeNode(2)
p3.right = TreeNode(1)

# Создаем дерево q: [1,1,2]
#     1
#    / \
#   1   2
q3 = TreeNode(1)
q3.left = TreeNode(1)
q3.right = TreeNode(2)

result3 = solution.isSameTree(p3, q3)
print(f'Дерево p = [1,2,1], дерево q = [1,1,2]')
print(f'Результат: {result3}\n') # False

# ----- Пример 4: пустые деревья. -----
print('Пример 4: оба дерева пустые.')
p4 = None
q4 = None
result4 = solution.isSameTree(p4, q4)
print(f'Дерево p = None, дерево q = None')
print(f'Результат: {result4}\n') # True

# ----- Пример 5: одно дерево пустое, другое нет. -----
print('Пример 5: одно дерево пустое, другое нет.')
p5 = None
q5 = TreeNode(1)
result5 = solution.isSameTree(p5, q5)
print(f'Дерево p = None, дерево q = [1]')
print(f'Результат: {result5}\n') # False

# ----- Пример 6: сложное дерево. -----
print('Пример 6: сложные одинаковые деревья.')
# Дерево p: [1,2,3,4,5,6,7]
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7
p6 = TreeNode(1)
p6.left = TreeNode(2)
p6.right = TreeNode(3)
p6.left.left = TreeNode(4)
p6.left.right = TreeNode(5)
p6.right.left = TreeNode(6)
p6.right.right = TreeNode(7)

# Дерево q: такое же
q6 = TreeNode(1)
q6.left = TreeNode(2)
q6.right = TreeNode(3)
q6.left.left = TreeNode(4)
q6.left.right = TreeNode(5)
q6.right.left = TreeNode(6)
q6.right.right = TreeNode(7)

result6 = solution.isSameTree(p6, q6)
print(f'Сложное дерево p и такое же дерево q')
print(f'Результат: {result6}') # True

# bool - означает логический тип данных (булевый тип), который принимает только 2 значения:
# True - истина, верно.
# False - ложь, неверно.

# None - означает пустое дерево.

# [1,2,3] означает дерево с корнем 1, левым потомком 2 и правым потомком 3.

# [1,null,2] означает дерево с корнем 1, без левого потомка и с правым потомком 2.
