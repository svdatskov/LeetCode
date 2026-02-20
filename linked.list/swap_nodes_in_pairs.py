# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
#
#
#
# Example 1:
#
# Input: head = [1,2,3,4]
#
# Output: [2,1,4,3]
#
# Explanation:
#
#
#
# Example 2:
#
# Input: head = []
#
# Output: []
#
# Example 3:
#
# Input: head = [1]
#
# Output: [1]
#
# Example 4:
#
# Input: head = [1,2,3]
#
# Output: [2,1,3]
#
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = head.next
        prev = None

        while head and head.next:
            if prev:
                prev.next = head.next

            prev = head

            next_node = head.next.next
            head.next.next = head
            head.next = next_node
            head = next_node

        return dummy



s = Solution()
result = s.swapPairs(ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))

while result:
    print(result.val)
    result = result.next



