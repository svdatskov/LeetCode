from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []

        if not root:
            return ans

        queue = deque([root])

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

            average_val = summ / level_size
            ans.append(average_val)

        return ans