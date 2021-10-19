n=int(input())
for _ in range(n):
    l=int(input())
    s=input()
    count=0
    flag=0
    sum=0
    for i in range(len(s)):
        if(s[i]=='U'):
            sum+=1
        else:
            sum-=1
        # print(sum)
        if(sum<0):
            # print("Coe")
            flag=1
        if(sum==0 and flag==1):
            count+=1
        if(sum>0):
            flag=0
    print(count)