# Даны корни двух бинарных деревьев p и q.
# Напишите функцию, чтобы проверить, являются ли они одинаковыми.

# Два бинарных дерева считаются одинаковыми, если они структурно идентичны,
# и узлы имеют одинаковые значения.

# Пример 1:
# Ввод: p = [1,2,3], q = [1,2,3]
# Вывод: true

# Пример 2:
# Ввод: p = [1,2], q = [1,null,2]
# Вывод: false

# Пример 3:
# Ввод: p = [1,2,1], q = [1,1,2]
# Вывод: false

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
