n=int(input())
string=input()
dictionary={}
dictionary[0]=1
sum=0
ans=0
for i in range(len(string)):
    if(string[i]=='X'):
        sum+=1
    else:
        sum-=1
    if(sum in dictionary):
        ans+=dictionary[sum]
        dictionary[sum]+=1
    else:
        dictionary[sum]=1
print(ans)

    