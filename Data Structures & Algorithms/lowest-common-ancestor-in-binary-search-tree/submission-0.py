# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lca = None
        def search(root):
            if not root:
                return None
            
            if root.val == p.val or root.val == q.val:
                self.lca = root
                return
            
            elif root.val > p.val and root.val < q.val:
                self.lca = root
                return
            
            elif root.val < p.val and root.val > q.val:
                self.lca = root
                return

            if root.val > p.val and root.val > q.val:
                search(root.left)
            else:
                search(root.right)
        search(root)
        return(self.lca)

            
