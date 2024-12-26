# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [] 
        que = deque([root])
        l_vals = []
        while(que):
            max_ = -2 ** 31
            for _ in range(len(que)):
                node = que.popleft()
                max_ = max(max_, node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            l_vals.append(max_)

        return l_vals

            
