# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
#
# Return the decimal value of the number in the linked list.
#
# The most significant bit is at the head of the linked list.
#
#
#
# Example 1:
#
#
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
# Example 2:
#
# Input: head = [0]
# Output: 0
#
#
# Constraints:
#
# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        dummy = head
        counter = 0

        while dummy:
            dummy = dummy.next
            counter += 1

        ans = 0
        capacity = 2 ** (counter - 1)

        while head:
            if head.val == 1:
                ans += capacity
            capacity /= 2
            head = head.next

        return ans


s = Solution()
print(s.getDecimalValue(ListNode(1, ListNode(0, ListNode(1)))))

