from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], minimum: int, maximum: int):
            if node is None:
                return maximum - minimum

            minimum = min(minimum, node.val)
            maximum = max(maximum, node.val)

            left_diff = dfs(node.left, minimum, maximum)
            right_diff = dfs(node.right, minimum, maximum)

            return max(left_diff, right_diff)

        return dfs(root, root.val, root.val)

s = Solution()
print(s.maxAncestorDiff(
    TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))),
             TreeNode(10, None, TreeNode(14, TreeNode(13))))))