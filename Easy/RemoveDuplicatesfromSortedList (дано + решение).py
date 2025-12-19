# Дан отсортированный список. Удалите все дубликаты так, чтобы каждый элемент
# встречался только один раз. Верните связанный список также в отсортированном виде.

# Пример 1:
# Input = [1,1,2]
# Output = [1,2]

# Пример 2:
# Input = [1,1,2,3,3]
# Output = [1,2,3]

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

head1 = ListNode(1, ListNode(1, ListNode(2))) # Input [1,1,2]
result1 = Solution().deleteDuplicates(head1)
output1 = []
while result1:
    output1.append(result1.val)
    result1 = result1.next
print('Пример 1: ', output1) # Output [1,2]

head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3))))) # Input [1,1,2,3,3]
result2 = Solution().deleteDuplicates(head2)
output2 = []
while result2:
    output2.append(result2.val)
    result2 = result2.next
print('Пример 2:', output2) # Output [1, 2, 3]
