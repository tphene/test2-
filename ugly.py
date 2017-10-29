def ugly(n):
        """
        :type n: int
        :rtype: int
        """

        ugly = [0]*n
        ugly[0]=1
        i2 = 0
        i3 = 0
        i5 = 0
        f2 = 2
        f3 = 3
        f5 = 5
        
        for i in range(1,n):
            print(f2,f3,f5)
            mini = min(f2,f3,f5)
            ugly[i] = mini
            
            if(f2==mini):
                i2+=1
                f2 = ugly[i2]*2

            if(f3==mini):
                i3+=1
                f3 = ugly[i3]*3

            if(f5==mini):
                i5+=1
                f5 = ugly[i5]*5
            
        #print(ugly)
        return ugly[-1]

print(ugly(3))