class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        currentNode=root
        stack=[]
        inorderSeq=[]
        while True:
            if currentNode is not None:
                stack.append(currentNode)
                currentNode = currentNode.left
                    
            elif(stack):
                currentNode = stack.pop()
                inorderSeq.append(currentNode.val)
                currentNode = currentNode.right
            else:
                break
                
        return inorderSeq      
       
