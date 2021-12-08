for _ in range(int(input())):
    n=int(input())
    dictionary={}
    count=1
    for i in range(n):
        h,m=map(int,input().split())
        key=str(h)+"#"+str(m)
        if(key in dictionary):
            dictionary[key]+=1
        
        else:
            dictionary[key]=1
        
        
    for i in dictionary:
        val=dictionary[i]
        count=max(val,count)
    print(count)
    