#l33t
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.a = 1
        def highttree(node):
            if(node == None):
                return 0
            else:
                ldia = highttree(node.left)
                rdia = highttree(node.right)
                self.a =  (max(self.a,ldia+rdia+1)) 
                return max(ldia,rdia)+1
        highttree(root)
        return self.a-1
        