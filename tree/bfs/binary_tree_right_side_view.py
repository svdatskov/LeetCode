from typing import Optional
from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        if not root:
            return ans

        queue = deque([root])

        while queue:
            nodes_in_current_section = len(queue)

            for i in range(nodes_in_current_section):
                node = queue.popleft()

                if i == 0:
                    ans.append(node.val)

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)

        return ans