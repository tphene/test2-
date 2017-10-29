s = '110001111000000'

def count_bin(s):
    groups = []
    c = s[0]
    count = 1
    
    for i in range(1,len(s)):
        if(s[i]==c):
            count+=1
        else:
            groups.append(count)
            count=1

        c = s[i]
    groups.append(count)
    
    fin_count =0 
    for i in range(1,len(groups)):
        fin_count+=min(groups[i],groups[i-1])

    return fin_count
        
    

print(count_bin(s))
    
