def happy(n):

    if(n/10==0):
        n = n * n
        print(n)
    while(n/10!=0):
        buffer = n
        sum = 0
        for i in str(buffer):
            sum += int(i)*int(i)

        if(sum==1):
            return True
        elif(sum/10==0):
            return False
        else:
            n = sum
    if(n==1):
        return True
    else:
        return False


