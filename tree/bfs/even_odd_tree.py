from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        queue = deque([root])
        current_level = 0

        while queue:
            level_size = len(queue)
            prev_val = None

            for _ in range(level_size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                if prev_val:
                    is_odd = current_level % 2
                    is_invalid_level_size = level_size != current_level

                    if (is_odd and prev_val >= node.val) or (not is_odd and prev_val <= node.val) or is_invalid_level_size:
                        return False

                prev_val = node.val

            current_level += 1

        return True

