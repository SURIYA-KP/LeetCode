# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        que = deque([root])
        swaps = 0
        while(que):
            vals = []
            position_map = dict()
            for i in range(len(que)):
                current = que.popleft()
                vals.append(current.val)
                position_map[current.val] = i 
                if current.left:
                    que.append(current.left)
                if current.right:
                    que.append(current.right)
            
            sorted_vals = vals.copy()
            sorted_vals.sort()
            for i in range(len(vals)):
                if vals[i] != sorted_vals[i]:
                    pos = position_map[sorted_vals[i]]
                    position_map[sorted_vals[i]] = i
                    position_map[vals[i]] = pos
                    vals[i], vals[pos] = vals[pos], vals[i]
                    swaps += 1
        return swaps

                
