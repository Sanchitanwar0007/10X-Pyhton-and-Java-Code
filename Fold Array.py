import array,math
n=int(input())
arr=array.array("i",[])
for i in range(n):
    num=int(input())
    arr.append(num)
m=int(input())
for i in range(m):
    for i in range(len(arr)//2):
        arr[i]=arr[i]+arr[(len(arr)-1)-i]
    if(len(arr)%2==0):
        arr=arr[0:len(arr)//2]
    else:
        arr=arr[0:len(arr)//2+1]
print(len(arr))
for i in arr:
    print(i)
    #Got 100%