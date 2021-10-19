# import math
# def factor(num):
#     count=0
#     for i in range(1,int(math.sqrt(num))+1):
#         if(num%i==0):
#             count+=1
#             if(num//i!=i):
#                 count+=1
#     return count
# def pairs(arr):
#     dict={}
#     for i in arr:
#         fac=factor(i)
#         if fac in dict:
#             dict[fac]+=1
#         else:
#             dict[fac]=1
#     result=0
#     for x in dict:
#         result+=(dict[x]*(dict[x]-1))//2
#     return result

# n=int(input())
# arr=list(map(int,input().split()))
# print(pairs(arr))
import math
def factors(num):
    ans=0
    for i in range(1,int(math.sqrt(num))+1):#int(math.sqrt(num))+1
        if(num%i==0):
            ans+=1 
            if(num//i!=i):  # num==16-->16//----->16//1==16// 16//2===>8  16//4==4
                ans+=1  
    return ans

def bars(arr):
    dict={}
    for i in range(len(arr)):
        fact=factors(arr[i])
        if fact in dict:
            dict[fact]+=1
        else:
            dict[fact]=1
    # print(dict)  #---> {3:1,5:1,4:1}
    ncr=0
    for i in dict:
        if(i>1):
            ncr+=(dict[i]*(dict[i]-1))//2
    print(ncr)
n=int(input())
arr=list(map(int,input().split()))
bars(arr)