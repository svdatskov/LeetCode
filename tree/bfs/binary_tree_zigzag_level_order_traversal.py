from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        if not root:
            return ans

        queue = deque([root])
        order = -1

        while queue:
            nodes_in_current_section = len(queue)
            section = [0] * nodes_in_current_section
            iterator = nodes_in_current_section - 1 if order else 0

            for _ in range(nodes_in_current_section):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                section[iterator] = node.val

                if order:
                    iterator -= 1
                else:
                    iterator += 1

            ans.append(section)
            order *= -1

        return ans