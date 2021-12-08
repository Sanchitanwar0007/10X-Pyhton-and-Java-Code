# n=int(input())
# k=int(input())
# arr=list(map(int,input().split()))
# arr.sort()
# i=0
# j=len(arr)-1
# ans=float('inf')
# while(i<j):
#     if(arr[i]+arr[j]<k):
#         if(abs(arr[i]+arr[j]-k)<ans):
#             ans=abs(arr[i]+arr[j]-k)
#         i+=1
#     elif(arr[i]+arr[j]>k):
#         if(abs(arr[i]+arr[j]-k)<ans):
#             ans=abs(arr[i]+arr[j]-k)
#         j-=1
#     else:
#         if(abs(arr[i]+arr[j]-k)<ans):
#             ans=abs(arr[i]+arr[j]-k)
#         i+=1
#         j-=1
#         break
# print(ans)
        
# your code goes here
n=int(input())
k=int(input())
arr=list(map(int,input().split()))
arr.sort()
i=0
j=len(arr)-1
ans=float('inf')
while(i<j):
    x=abs(arr[i]+arr[j]-k)
    if(arr[i]+arr[j]<k):
    	
        if(x<ans):
            ans=x
        i+=1
    elif(arr[i]+arr[j]>k):
        if(x<ans):
            ans=x
        j-=1
    else:
        if(x<ans):
            ans=x
        i+=1
        j-=1
        break
print(ans)