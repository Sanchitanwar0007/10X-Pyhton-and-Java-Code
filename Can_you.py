# r=10**6
# c=10**6
# mat=[]
# for i in range(r):
#     a=[int(x) for x in input().split()]
#     mat.append(a)\
val=10**5
for _ in range(int(input())):
    
    n=int(input())
    ans=0
    for i in range(n):
        r,c=map(int,input().split())
        if(r==c):
            ans+=1
    
        # print(r+c)
    
    print(ans)
        # print(r,c)