# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(current_1, current_2, level):
            if current_1.left:
                dfs(current_1.left, current_2.right, level + 1)
                dfs(current_1.right, current_2.left, level + 1)
            if level & 1:
                temp = current_1.val
                current_1.val = current_2.val
                current_2.val = temp
        if root.left:
            dfs(root.left, root.right, 1)
        return root
