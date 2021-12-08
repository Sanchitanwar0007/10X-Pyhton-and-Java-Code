def is_pal(s,start,limit):
    if(limit<0):
        return
    start.append(s[limit])
    is_pal(s,start,limit-1)
    
for _ in range(int(input())):
    s=input()
    arr=[]
    is_pal(s,arr,len(s)-1)
    s2="".join(arr)
    if(s==s2):
        print(True)
    else:
        print(False)    
    