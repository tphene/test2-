class Node:
    def __init__(self,val):
        self.l = None
        self.r = None
        self.val = val
    
class tree:
    def __init__(self):
        self.root = None
    
    def get_root(self):
        return self.root

    def add(self,val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self.add_node(val,self.root)
    
    def add_node(self,val,node):
        if(val<node.val):
            if(node.l == None):
                node.l = Node(val)
            else:
                self.add_node(val,node.l)
        
        else:
            if(node.r == None):
                node.r = Node(val)
            else:
                self.add_node(val,node.r)

    def Inorder(self,node):
        if(node == None):
            return
        else:
              
            self.Inorder(node.l)                    
            self.Inorder(node.r) 
            print(node.val)
t = tree()
t.add(1)
t.add(5)
t.add(6)
t.add(2)
t.add(9)
t.add(3)

t.Inorder(t.get_root())




        