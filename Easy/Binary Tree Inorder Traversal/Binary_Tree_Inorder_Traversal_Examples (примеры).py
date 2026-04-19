from Binary_Tree_Inorder_Traversal import *

# Как это выглядит логически:
# Для каждого узла:
# 1. Обойти левое поддерево.
# 2. Записать значение узла.
# 3. Обойти правое поддерево.

# Пример простого дерева:
#     1
#      \
#       2
#      /
#     3

# Порядок вызовов:
# dfs(1)
#  L- dfs(None)
#  L- add 1
#  L- dfs(2)
#      L- dfs(3)
#          L- add 3
#      L- add 2

# --------------------------------------------------------

# Пример 1: root = [1, null, 2, 3]
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

print("Пример 1:", Solution().inorderTraversal(root1))

# --------------------------------------------------------

# Пример 2: root = [1,2,3,4,5,null,8,null,null,6,7,9]

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)

root2.left.right.left = TreeNode(6)
root2.left.right.right = TreeNode(7)

root2.right.right = TreeNode(8)
root2.right.right.left = TreeNode(9)

print("Пример 2:", Solution().inorderTraversal(root2))

# --------------------------------------------------------

# Пример 3: root = []
print("Пример 3:", Solution().inorderTraversal(None))

# --------------------------------------------------------

# Пример 4: root = [1]
root4 = TreeNode(1)
print("Пример 4:", Solution().inorderTraversal(root4))

# --------------------------------------------------------