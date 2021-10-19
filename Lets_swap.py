#index  =   [1,2,3,4,5]
#arr    =   [1 4 2 3 5]
#min(i,arr)=[1,2,2,3,5]
#max(i,arr)=[1,4,3,4,5]
# max(min(i,arr))=5
# min(max(i,arr))=1
# 5-1=4*2
#ans=max-min=> 0+2+1+1+0=4
#4+8=12


# your code goes here
n=int(input())
arr=[int(x) for x in input().split()]
mini=[]
maxi=[]
ans=0
# print(len(mini),len(maxi))
for i in range(len(arr)):
    # print(i)
    mini.append(min(arr[i],i+1))
    maxi.append(max(arr[i],i+1))
for i in range(len(arr)):
    ans+=abs(mini[i]-maxi[i])

diff=abs(max(mini)-min(maxi))
ans+=2*diff
print(ans)