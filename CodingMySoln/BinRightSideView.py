# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#Ex 1:Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <--- 3

class Solution:
	def __init__(self):
		self.height = -1
    def rightSideView(self, root: TreeNode) -> List[int]:
        ret = []
        temp = root
        if temp == None:
        	return None
        if temp.val == root.val:
        	return ret
        temp = rightSideView(temp.right)
        temp = rightSideView(temp.left)
    	return temp