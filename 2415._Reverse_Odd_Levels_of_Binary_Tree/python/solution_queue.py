# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        main_que = deque([root])
        odd_que = deque()
        odd_stack = []
        level = 0
        while(main_que):
            for _ in range(len(main_que)):
                current = main_que.popleft()
                if current.left:
                    main_que.append(current.left)
                    main_que.append(current.right)
                if level % 2 == 1:
                    odd_que.append(current)
                    odd_stack.append(current.val)

            if level % 2 == 1:
                for _ in range(len(odd_stack)):
                    current_node = odd_que.popleft()
                    current_val = odd_stack.pop()
                    current_node.val = current_val
            
            level += 1
        return root
                
