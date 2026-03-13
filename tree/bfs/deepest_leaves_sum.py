from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans = 0

        if not root:
            return ans

        queue = deque([root])

        while queue:
            nodes_in_current_section = len(queue)
            ans = 0

            for _ in range(nodes_in_current_section):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                ans += node.val

        return ans