# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
#
# Input: head = [1], n = 1
# Output: []
# Example 3:
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
# Constraints:
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
#
# Follow up: Could you do this in one pass?

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        counter = 1

        while fast.next:
            if counter >= n:
                slow = slow.next
            fast = fast.next
            counter += 1

        slow.next = slow.next.next

        return dummy.next

s = Solution()
output = s.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
while output:
    print(output.val)
    output = output.next

