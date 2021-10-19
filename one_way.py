def isEditDistanceOne(s1, s2):
    n=len(s1)
    m=len(s2)
    if(abs(n-m)>1 or s1==s2):
        return False
    i=0   #abcde
    j=0   #abdcde
    count=0
    while(i<len(s1) and j<len(s2)):
        if(s1[i]==s2[j]):
            i+=1
            j+=1
        elif(count==1):
            return False
        else:
            count=1
            if(n>m):
                i+=1
            if(n<m):
                j+=1
            else:
                i+=1
                j+=1
    return True

            


for _ in range(int(input())):
    input_string1, input_string2 = input().split()
    print(isEditDistanceOne(input_string1, input_string2))