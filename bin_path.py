class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

    
a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.left.right = TreeNode(5)
a.right.left = TreeNode(6)
a.right.right = TreeNode(7)

def leaf(node):
    if(node.left==None and node.right==None):
        return True
    return False

def create_path(node,ans,path):
    path.append(node.val)
    print(node.val)
    if(leaf(node)):        
        ans.append(path[0:])
    else:
        if(node.left!=None):
            create_path(node.left,ans,path[0:])
        if(node.right!=None):
            create_path(node.right,ans,path[0:])          

def binaryTreePaths(root):
    ans = []
    create_path(root,ans,[])
    return ans

print(binaryTreePaths(a))

        
