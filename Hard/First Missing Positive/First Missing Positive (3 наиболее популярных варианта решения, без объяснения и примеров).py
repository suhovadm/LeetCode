# Варианты решения.

# Вариант 1. Классическое решение с перестановкой чисел "на свои места".

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

# ---------------------------------------------------------------------------------

# Вариант 2. Немного упрощённый.

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

# ---------------------------------------------------------------------------------

# Вариант 3. Максимально простой, но его не примет LeetCode.

class Solution:
    def firstMissingPositive(self, nums):
        s = set(nums)
        i = 1
        while i in s:
            i += 1
        return i
    
# ---------------------------------------------------------------------------------
