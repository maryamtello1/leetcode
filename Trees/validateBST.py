# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

#NOTES
#Will be depth first search which will involve recursion. 
#create a helper function for recursion
#find the base case
#write the recursive case for both left and right parts of the tree 
#and then call it on the root and return the solution

class TreeNode:
   def __init__(self,val):
      self.val=val
      self.left=None
      self.right=None


class Solution:
   def valideBST(self,root):
      def valid(node, left,right):
         if not node:
            return True
         if not(node.val<right and node.val>left):
            return False
         return(valid(node.left,left,node.val)and valid(node.right,node.val,right))
      return valid(root,float("-inf"),float("inf"))
         
#   3
#  / \
# 2    5
#/ \  /  \
#1  1 4   6

root= TreeNode(3)
root.left=TreeNode(2)
root.right=TreeNode(4)
root.left.left=TreeNode(1)
root.right.right=TreeNode(6)
