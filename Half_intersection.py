def sort_half(s):
    mid=len(s)//2
    list=[]
    for i in range(mid,len(s)):
        list.append(s[i])
    # print(list)
    for i in range(len(list)):
        j=i
        while(j>0 and ord(list[j])<ord(list[j-1])):
            list[j],list[j-1]=list[j-1],list[j]
            j-=1
    string=""
    for i in range(0,mid):
        string+=s[i]+""
    for i in list:
        string+=i+""
    return string
s=input()
print(sort_half(s))