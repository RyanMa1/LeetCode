#Ex 1:
# Input:
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Time Complexity is: O(N) Space Complexity(In place): O(height)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #note: write guard clauses before
        if root == None:
        	return None
        print()
		left = root.left
		root.left = right
		root.right = left
		invertTree(root.left)
		invertTree(root.right)
		return root


