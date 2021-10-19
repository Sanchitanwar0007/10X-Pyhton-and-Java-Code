def longest_substring(s):
    dict={}
    i=0
    j=0
    maxi=0
    while(True):
        first=True
        second=True
        while(i<len(s)):
            first=False
            if s[i] not in dict:
                dict[s[i]]=1
            else:
                dict[s[i]]+=1
            temp=s[i]
            i+=1
            if(dict[temp]==2):
                break
            else:
                maxi=max(maxi,i-j)
            
        
        
        while(j<i):
            second=False
            dict[s[j]]-=1
            temp2=s[j]
            j+=1
            if(dict[temp2]==1):
                break
        
        if(first==True and second==True):
            break
    return maxi
n=int(input())
for _ in range(n):
    s=input()
    print(longest_substring(s))
