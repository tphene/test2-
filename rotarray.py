a = [4,6,7,1,2,3]
#a = [0,1,2,3,4,5]
#a= [5, 6, 1, 2, 3, 4]

i = 0
j = len(a)-1



def search_min(a):
    low = 0
    high = a.__len__()-1
    while(low<=high):
        print(high)
        print(low)
        if(a[low]<=a[high]):
            return a[low]
        mid = (high + low)/2
        
        if(a[mid]>a[low]):
            low = mid + 1
        else:
            high = mid
    
    #return -1

t = search_min(a)
print('result',t)

