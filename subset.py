a = [1,2,3,4,5,6,7,8,9]
target = 9
k = 3
res = []
a.sort()
# This uses dfs(depth first search recursively)
def create(a,index,path,res,target,k):
    if(target==0 and len(path)==k):
        res.append(path)
        return
    if(target<0):
        return 
    for i in range(index,len(a)):
        create(a,i+1,path+[a[i]],res,target-a[i],k)
    
    return res

print(create(a,0,[],res,target,k))

