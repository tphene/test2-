a = [[1,2,3,4],[5,6,7,8],[9,10,11,14]]
a = [[1,2],[3,4]]
a = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]

def search(a,key):
    row = len(a)
    col = len(a[0])
    #a = [0,1,2,3,4,5,6,7,8,9,10,11]
    i = 0
    j = row * col -1

    while(i<=j):
        m = (i+j)/2
        mi = int(m/col)
        mj = int(m%col)
        if(a[mi][mj]==key):
            return True
        elif(a[mi][mj]>key):
            j = m-1
        else:
            i = m+1

    return False
print(search(a,5))
