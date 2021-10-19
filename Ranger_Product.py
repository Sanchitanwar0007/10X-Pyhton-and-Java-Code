# def divide(num1,num2):
#     flag1=0
#     flag2=0
#     if(num1<0):
#         flag1=1
#         num1=-1*num1
#     if(num2<0):
#         flag2=1
#         num2=-1*num2
#     res=0
#     while(num1>=num2):
#         num1=num1-num2
#         res+=1
#     if((flag1==1 and flag2==0) or (flag1==0 and flag2==1) ):
#         return -1*res
#     else:
#         return res
# n=int(input())
# for j in range(n):
#     num=int(input())
#     arr=list(map(int,input().split()))
#     mul=1
#     for i in range(len(arr)):
#         mul*=arr[i]
#     res=[]
#     for k in range(len(arr)):
#         # print(k)
#         res.append(divide(mul,arr[k]))
#     for p in res:
#         print(p,end=" ")
#     print()
def product(arr):
    length=len(arr)
    if(length==1):
        return 1
    left_mul=[0]*length
    right_mul=[0]*length
    left_mul[0]=1
    right_mul[0]=1
    for i in range(1,length):
        left_mul[i]=arr[i-1]*left_mul[i-1]
    arr.reverse()
    for i in range(1,length):
        right_mul[i]=right_mul[i-1]*arr[i-1]
    right_mul.reverse()
    # print(left_mul,right_mul)
    for i in range(length):
        arr[i]=left_mul[i]*right_mul[i]
    return arr
n=int(input())
for i in range(n):
    num=int(input())
    arr=list(map(int,input().split()))
    a=product(arr)
    for i in a:
        print(i,end=" ")
    print()