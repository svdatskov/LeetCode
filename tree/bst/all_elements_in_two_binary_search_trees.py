from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        tree1 = []
        tree2 = []
        def dfs(root, arr):
            if not root:
                return

            dfs(root.left, arr)

            arr.append(root.val)

            dfs(root.right, arr)

        dfs(root1, tree1)
        dfs(root2, tree2)

        merged_array = tree1 + tree2
        merged_array.sort()

        return merged_array



