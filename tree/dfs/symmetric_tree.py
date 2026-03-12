# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
#
#
#
# Example 1:
#
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:
#
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(left_node, right_node) -> bool:
            if not right_node and not left_node:
                return True

            if not right_node or not left_node:
                return False

            return (right_node.val == left_node.val and
                    is_mirror(left_node.left, right_node.right) and
                    is_mirror(left_node.right, right_node.left))

        return is_mirror(root.left, root.right)