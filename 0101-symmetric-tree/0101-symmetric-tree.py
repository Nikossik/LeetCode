# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isTreeSymmetric(self, left, right):
        if left is None and right is None:
            return True
        if(left is None and right is not None) or (left is not None and right is None):
            return False
        if left.val != right.val:
            return False
        return self.isTreeSymmetric(left.left, right.right) and self.isTreeSymmetric(left.right, right.left)
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isTreeSymmetric(root.left, root.right)
        