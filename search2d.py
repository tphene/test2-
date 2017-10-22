a = [[1,2,3,4],[5,6,7,8],[9,10,11,14]]
a = [[1,2],[3,4]]
a = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
row = len(a)
col = len(a[0])
#a = [0,1,2,3,4,5,6,7,8,9,10,11]
i = 0
j = row * col -1
key = 50
while(i<=j):
    m = (i+j)/2
    mi = m/col
    mj = m%col
    if(a[mi][mj]==key):
        print(mi,"x",mj)
        break
    elif(a[mi][mj]>key):
        j = m-1
    else:
        i = m+1


