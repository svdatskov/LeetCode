# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
#
#
#
# Example 1:
#
#
# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:
#
#
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
#

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        last_unique_element = head

        while dummy:
            if dummy.val != last_unique_element.val:
                last_unique_element.next = dummy
                last_unique_element = last_unique_element.next
            elif not dummy.next:
                last_unique_element.next = None

            dummy = dummy.next

        return head

s = Solution()
output = s.deleteDuplicates(ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3))))))

while output:
    print(output.val)
    output = output.next


