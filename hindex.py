a = [3,0,1,6,5]

n = len(a)
a.sort()
print(a)

# Brute force mechanism
'''
count = 0
for i,e in enumerate(a):
    if(e>i):
        #print(a[i])
        count +=1
    else:
        break
print(count)
'''
'''
b = [0]*(n+1)

for i,e in enumerate(a):
    if(e>=n):
        b[n]+=1
    else:
        b[i]+=1
count = 0
for i in range(n,-1,-1):
    count+=b[i]
    if(count>i):
        print(count)
        break
'''
'''
n = len(a)
l,r = 0,n-1
while l <= r:
    mid = (l+r)/2
    if a[mid] >= n-mid:
        #print(mid)
        r = mid-1
    else:
        l = mid+1

print(n-l)
'''
n = len(a)
l = 0
r = n-1
while(l<=r):
    mid = (l+r)/2
    if(a[mid]>=n-mid):
        r = mid -1
    else:
        l = mid +1

print(n-l)
print(r)






