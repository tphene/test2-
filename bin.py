a = [3,0,6,1,5]
a.sort()

i = 0
j = a.__len__()-1

e = 1
while(i<=j):
    mid = (i+j)/2
    if(a[mid]==e):
        print(mid)
        break
    elif(a[mid]>e):
        j = mid-1
    else:
        i = mid+1
        


