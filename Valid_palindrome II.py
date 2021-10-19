def isPal_del(str):
    if(str==str[::-1]):
        return True
    j=len(str)-1
    for i in range(len(str)):
        if(str[i] != str[j]):
            s_new=str[:i]+str[i+1:]
            s_new2=str[:j]+str[j+1:]
            if(s_new==s_new[::-1] or s_new2==s_new2[::-1]):
                return True
        else:
            j-=1
    return False
        
for _ in range(int(input())):
    str=input()
    print(isPal_del(str))

     
