def count(s):
    c0=0
    c1=0
    c2=0
    key=(c1-c0),"#",(c2-c1)
    dict={}
    dict[key]=1
    ans=0
    for i in s:
        if(i=='a'):
            c0+=1
        elif(i=='b'):
            c1+=1
        elif(i=='c'):
            c2+=1
        key=(c1-c0),"#",(c2-c1)
        if(key in dict):   
            ans+=dict[key]
            dict[key]+=1
        else:
            dict[key]=1
    return ans
n=int(input())
for i in range(n):
    s=input()
    print(count(s))