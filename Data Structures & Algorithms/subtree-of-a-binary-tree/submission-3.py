# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val != q.val:
                return False
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        
        # stack = []
        # curr = root
        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     curr = stack.pop()
        #     if sameTree(curr, subRoot):
        #         return True
        #     curr = curr.right
        
        # return False

        if not subRoot:
            return True
        if not root:
            return False
        if sameTree(subRoot, root):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
        
        
            
        

        
        
        