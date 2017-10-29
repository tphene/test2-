

def result(n):
    a = ['0']
        
    i=0
    while(i<n):
        l = []
        for j in a:
            t = j+'0'
            l.append(t)
        for j in range(len(a)-1,-1,-1):
            t = a[j]+'1'
            l.append(t)
        a = l
        i+=1
        
    res= []
    for i in a:
        t = int(i,2)
        res.append(t)
    print(res)
result(3)



