# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self, rootNode: TreeNode)
        self rootNode = rootNode
    
    def DFS(self, node, tree, path):
        if not tree or tree.val == needle:
            return path

        path.append(stack.val)

        left = self.DFS(node,tree.left,path)
        if left:
            return left
        right = self.DFS(node,tree.right,parht)
        if right:
            return right

    def lastCommon(self,listOne,listTwo):
        lastMatch = None

        for i,j in zip(listOne,listTwo):
            if i==j:
                lastMatch = i

        return lastMatch

    def common_ancestor(self,one,two):
        onePath = self.DFS(one,self.root, [])
        twoPath = self.DFS(two,self.root, [])
        
        return slef.lastCommon(onePath,twoPath)

if __name__ == '__main__':
    root = TreeNode(3)
￼    left = TreeNode(4)
￼    right = TreeNode(5)
￼    left_left = TreeNode(1)
￼    left_right = TreeNode(2)
￼
￼    root.left = left
￼    root.right = right
￼    root.left.left = left_left
￼    root.left.right = left_right
￼
    Solution(root)
