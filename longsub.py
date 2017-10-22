def longsub(nums):   
    d = {}
    for i in nums:
        if(i in d):
            d[i]+=1
        else:
            d[i]=1
    
    value = max(d.values())

    for i in d:
        if(d[i]==value):
            key = i

    maxval = value
    
    l=0
    f=0
    for i,e in enumerate(nums):
        if(e == key): 
            if(value==maxval):
                f = i
                print('f'+str(f))
            elif(value==1):
                l = i
                print('l'+str(l))
                break
            value-=1

    return (l-f+1)

print(longsub([1,2,2,3,1,4,2]))