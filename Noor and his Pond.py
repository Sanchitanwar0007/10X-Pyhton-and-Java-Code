for _ in range(int(input())):
    num=int(input())
    s=[]
    e=[]
    for i in range(num):
        x,y=map(int,input().split())
        s.append(x)
        e.append(y)
    s.sort()
    e.sort()
    i=0
    j=0
    ans=0
    while(j<len(s)):
        if(e[j]>=s[i]):
            ans=max(ans,j-i)
            i+=1
        else:
            j+=1
    ans=max(ans,j-i)
    print(ans)

        
