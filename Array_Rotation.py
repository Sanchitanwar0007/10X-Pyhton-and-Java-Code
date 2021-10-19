def left_rotation(arr,num):
    list=[0]*len(arr)
    for i in range(len(arr)):
        swap_pos=abs(i-num+len(arr))%len(arr)
        list[swap_pos]=arr[i]
    arr=list
    return arr
def right_rotation(arr,m):
    temp=[0]*m
    j=0
    for i in range(len(arr)-m,len(arr)):
        temp[j]=arr[i]
        j+=1

    list=[0]*len(arr)
    for i in range(len(temp)):
        list[i]=temp[i]

    for i in range(len(arr)-m):
        list[j]=arr[i]
        j+=1
    arr=list
    return arr
   
total=0
total_l=0
total_r=0
n,q=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(q):
    dir,num=input().split()
    num=int(num)
    if(dir=="L"):
        total_l+=num
    elif(dir=="R"):
        total_r+=num
# print(total_l,total_r)
if(total_l>total_r):
    total=total_l-total_r
    total=total%n
    arr=left_rotation(arr,total)
else:
    total=total_r-total_l
    total=total%n
    arr=right_rotation(arr,total)
for i in arr:
    print(i,end=" ")

# 5 4
# 1 2 3 4 5
# L 2
# R 4
# L 3
#Rajan Sharma Code here: ===>
    # n,k=map(int,input().split())
    # l=list(map(int,input().split()))[:n]
    # c1=0
    # for i in range(k):
    #     c,s=input().split()
    #     s=int(s)
    #     if(c=='L'):
    #         c1+=s
    #     else:
    #     	  c1+=n-s
    # c1=c1%n
    # l = l[c1:] + l[:c1]
    # print(*l)
