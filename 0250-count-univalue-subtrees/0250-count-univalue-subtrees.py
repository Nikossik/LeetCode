# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.counter = 0

        def helper(node):
            if node is None:
                return True
            isleft = helper(node.left)
            isright = helper(node.right)

            if isleft and isright:
                if node.left and node.val != node.left.val:
                    return False
                if node.right and node.val != node.right.val:
                    return False
                self.counter += 1
                return True
            return False
        helper(root)
        return self.counter
        