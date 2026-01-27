# Дано бинарное дерево, найдите минимальную глубину.
# Минимальная глубина - это количество узлов на кратчайшем пути от корневого узла до
# ближайшего листового узла.

# Примечание: лист - это узел без потомков.

# Пример 1:
# Ввод: root = [3,9,20,null,null,15,7]
# Вывод: 2

# Пример 2:
# Ввод: root = [2,null,3,null,4,null,5,null,6]
# Вывод: 5

# Ограничения:
# Количество узлов в дереве находится в диапазоне [0, 105].
# -1000 <= Node.val <= 1000

# Импортируем тип Optional для аннотации типов.
from typing import Optional

# Заводим класс узла бинарного дерева.
# Каждый узел содержит:
# val - значение узла (по умолчанию 0)
# left - левый потомок (по умолчанию None)
# right - праый потомок (по умолчанию None)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Заводим класс Solution, как того требует LeetCode.
class Solution:
    # Заводим метод minDepth (минимальная глубина).
    # Метод принимает корень дерева root и возвращает целое число (минимальную глубину).
    # Тип аргумента Optional[TreeNode] может быть None для пустого дерева.
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # Базовый случай рекурсии.
        # Если root равен None (пустое дерево или достигнут конец ветви),
        # возвращаем 0 (глубина пустого дерева = 0).
        if not root:
            return 0

        # Если у текущего узла нет левого потомка,
        # возвращаем: 1 (текущий узел) + минимальная глубина ПРАВОГО поддерева.
        # В данном случае, мы проверяем только root.left.
        if not root.left:
            return 1 + self.minDepth(root.right)

        # Если у текущего узла нет правого потомка,
        # возвращаем: 1 (текущий узел) + минимальная глубина ЛЕВОГО поддерева.
        if not root.right:
            return 1 + self.minDepth(root.left)

        # Общий случай.
        # Если у узла есть оба потомка, возвращаем: 1 (текущий узел) +
        # минимум из глубин двух поддеревьев.
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

# Пример 1: [3,9,20,null,null,15,7]
print('Пример 1: [3,9,20,null,null,15,7]')
print('Ожидаемый результат: 2')

# Создаем дерево:       3
#                      / \
#                     9   20
#                        /  \
#                       15   7

# Кратчайший путь: 3 -> 9 (глубина 2).

root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

solution = Solution()
result1 = solution.minDepth(root1)
print(f'Результат: {result1}\n')

# Пример 2: [2,null,3,null,4,null,5,null,6]
print('Пример 2: [2,null,3,null,4,null,5,null,6]')
print('Ожидаемый результат: 5')

# Создаем дерево: 2
#                  \
#                   3
#                    \
#                     4
#                      \
#                       5
#                        \
#                         6

# Кратчайший путь: 2 -> 3 -> 4 -> 5 -> 6 (глубина 5).

root2 = TreeNode(2)
root2.right = TreeNode(3)
root2.right.right = TreeNode(4)
root2.right.right.right = TreeNode(5)
root2.right.right.right.right = TreeNode(6)

result2 = solution.minDepth(root2)
print(f'Результат: {result2}\n')

# Пример 3: Пустое дерево.
print('Пример 3: Пустое дерево []')
print('Ожидаемый результат: 0')

# Кратчайший путь: 0 (глубина 0).

result3 = solution.minDepth(None)
print(f'Результат: {result3}\n')

# Пример 4: Дерево с одним узлом.
print('Пример 4: Дерево с одним узлом [1]')
print('Ожидаемый результат: 1')

# Кратчайший путь: 1 (глубина 1).

root4 = TreeNode(1)
result4 = solution.minDepth(root4)
print(f'Результат: {result4}\n')

# Пример 5: Сбалансированное дерево.
print('Пример 5: Сбалансированное дерево: [1,2,3,4,5,6,7]')
print('Ожидаемый результат: 3')

# Создаем дерево:       1
#                      / \
#                     2   3
#                    / \ / \
#                   4  5 6  7

# Кратчайший путь: 1 -> 2 -> 4 (по левому краю 3), или 1 -> 3 -> 6 (по правому краю 3).

root5 = TreeNode(1)
root5.left = TreeNode(2)
root5.right = TreeNode(3)
root5.left.left = TreeNode(4)
root5.left.right = TreeNode(5)
root5.right.left = TreeNode(6)
root5.right.right = TreeNode(7)

result5 = solution.minDepth(root5)
print(f'Результат: {result5}\n')

# Пример 6: Только левые потомки.
print('Пример 6: дерево, где только левые потомки [1,2,null,3,null,4]')
print('Ожидаемый результат: 4')

# Создаем дерево:     1
#                    /
#                   2
#                  /
#                 3
#                /
#               4

# Кратчайший путь: 1 -> 2 -> 3 -> 4 (глубина 4).

root6 = TreeNode(1)
root6.left = TreeNode(2)
root6.left.left = TreeNode(3)
root6.left.left.left = TreeNode(4)

result6 = solution.minDepth(root6)
print(f'Результат: {result6}')