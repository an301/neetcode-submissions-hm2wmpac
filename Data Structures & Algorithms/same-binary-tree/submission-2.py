# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # def dfs(curr):
        #     if not curr:
        #         return []
        #     order = []
        #     stk = [curr]
        #     while stk:
        #         curr = stk.pop()
        #         if curr == 'None':
        #             order.append(curr)
        #         else:
        #             order.append(curr.val)
        #         if curr != 'None':
        #             if curr.right:
        #                 stk.append(curr.right)
        #             else:
        #                 stk.append('None')
        #             if curr.left:
        #                 stk.append(curr.left)
        #             else:
        #                 stk.append('None')
        #     return order
        
        # stk1 = dfs(p)
        # stk2 = dfs(q)

        # return stk1 == stk2

        def dfs(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            
            return dfs(p.left,q.left) and dfs(p.right,q.right)
        
        return dfs(p,q)

