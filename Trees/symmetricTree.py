class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

#because it has to be vertically symmetric, a dfs approach would work best 
#create a helper recursive function and call it on the root
#base case is when there are no longer nodes to traverse 
#create simplest recursive case and call it on both left and right subtrees

class Solution:
    def isSymmetric(self,root):
        def helper(leftNode,rightNode):
            if not leftNode and not rightNode:
                return True
            if not leftNode or not rightNode:
                return False 
            return(leftNode.val==rightNode.val) and helper(leftNode.left,rightNode.right) and helper(leftNode.right,rightNode.left)
        return helper(root.left,root.right)
            


