from collections import deque
class treeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def levelOrder(root):
    result=[]
    if not root:
        return([])
    q=deque([root])
    while q:
        currentLevel=[]
        levelSize=len(q)
        for i in range(levelSize):
            node = q.popleft()  # deque from the front, pops root
            currentLevel.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(currentLevel)
    return result 

tree=treeNode(3)
tree.left=treeNode(5)
tree.right=treeNode(6)
print(levelOrder(tree))




    