def isSubsequences(s,str):
    max=0
    i=0
    j=0
    while(i<len(s) and j<len(str)):
        if(s[i]==str[j]):
            j+=1
        i+=1
    if(j==len(str)):
        max=len(str)
    return max
s=input()
dict_str=input()
list=dict_str.split(' ')
maxi=float('-inf')
for i in range(len(list)):
    m=isSubsequences(s,list[i])
    if(m>maxi):
        maxi=m
print(maxi)

