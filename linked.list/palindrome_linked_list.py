# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,2,1]
# Output: true
# Example 2:
#
#
# Input: head = [1,2]
# Output: false
#
#
# Constraints:
#
# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
#
#
# Follow up: Could you do it in O(n) time and O(1) space?

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None

        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True

s = Solution()

print(s.isPalindrome(ListNode(1, ListNode(2))))

