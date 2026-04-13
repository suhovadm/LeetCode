from typing import List, Optional

# Класс-заглушка для LeetCode. IDE будет ругаться, потому что видит структуру,
# LeetCode же всё это проигнорирует и всё заработает как надо.
# На красные подчёркивания просто не обращаем внимания, всё будет хокейно.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def build(left, right):
            if left > right:
                return None

            mid = (left + right + 1) // 2

            node = TreeNode(nums[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node

        return build(0, len(nums) - 1)

# Если использовать class TreeNode, то LeetCode выдаст ошибку по типу вот такой:
# TypeError: <__main__.TreeNode object ...> is not valid value for the expected return type TreeNode