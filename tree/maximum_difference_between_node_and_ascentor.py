from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                min_value = left[1]
                max_value = left[0]
                if abs(left[0] - left[1]) < abs(right[0] - right[1]):
                    min_value = right[1]
                    max_value = right[0]

                return max(max_value, node.val), min(min_value, node.val)


            if left:
                return max(left[0], node.val), min(left[1], node.val)

            if right:
                return max(right[0], node.val), min(right[1], node.val)

            return node.val, node.val

        result = dfs(root)
        return abs(result[1] - result[0])

s = Solution()
print(s.maxAncestorDiff(TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))), TreeNode(10, None, TreeNode(14, TreeNode(13))))))