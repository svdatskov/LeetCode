# Definition for a binary tree node.

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = 0

        if not root:
            return ans

        queue = deque([root])
        max_summ = float("-inf")
        level = 1

        while queue:
            level_size = len(queue)
            summ = 0

            for _ in range(level_size):
                node = queue.popleft()

                summ += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if summ > max_summ:
                max_summ = summ
                ans = level

            level += 1

        return ans

