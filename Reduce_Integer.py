import array
n =int(input())
arr= array.array("i",[])
for i in range(n):
    arr.append(int(input()))
if(len(arr)>=2):
    sum=arr[0]+arr[1]
else:
    sum=arr[0]
for i in range(2,len(arr)):
    if(i%2!=0):
        sum+=arr[i]
    else:
        sum-=arr[i]
print(sum)




#For O(1) space complexity:
import array
n =int(input())
sum=int(input())
for i in range(1,n):
    num=int(input())
    if(i==1):
        sum+=num
    else:
        if(i%2==0):
            sum-=num
        else:
            sum+=num
print(sum)

