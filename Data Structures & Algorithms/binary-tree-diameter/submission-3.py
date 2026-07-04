# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # maxDiam = [0]
        # def dfs(root):
        #     if not root:
        #         return 0
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     maxDiam[0] = max(maxDiam[0], left + right)
        #     return 1 + max(left, right)
        
        # dfs(root)
        # return maxDiam[0]


        
        def dfs(root):
            if not root:
                return 0, 0
            
            leftHeight, leftDiam = dfs(root.left)
            rightHeight, rightDiam = dfs(root.right)
            height = 1 + max(leftHeight, rightHeight)
            diam = max(leftDiam, rightDiam, leftHeight + rightHeight)
            return height, diam
        
        x = dfs(root)
        return x[1]

    

        


