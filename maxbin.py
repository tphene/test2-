class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
    def construct(nums,l,r,node):
        node = TreeNode(max(nums[l:r]))
        index = nums.index(max(nums[l:r]))
        if(index>0):
            construct(nums,0,index-1,node.left)
        if(index<len(nums)-1):
            construct(nums,index+1,len(nums)-1,t.right)
            
            
        
    t = TreeNode(max(nums))
    i = nums.index(max(nums))
    if(i>0):
        construct(nums,0,i-1,t.left)
    if(i<len(nums)-1):
        construct(nums,i+1,len(nums)-1,t.right)
    
    def print(t):
        if(t==None):
            return 
        else:
            