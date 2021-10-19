n=int(input())
arr=list(map(int,input().split()))
j=1
start=-1
end=-1
count=0
flag=1
list=[]
for i in range(n-1):
    if(arr[j]>arr[i]):
        count+=1
        if(flag==1):
            start=i
            flag=0
    else:
        flag=1
        # max=count
        if(count>0):
            list.append(start)
            list.append(j-1)
        count=0
    j+=1
    if(count>0 and j==n):
        list.append(start)
        list.append(j-1)
max=0
# print(list)
for i in range(1,len(list)):
    if(i%2!=0):
        num=list[i]-list[i-1]
        if(num>max):
            max=num
            start=list[i-1]
            end=list[i]
if(len(arr)==1):
    print(1,end=" ")
    print(1,end=" ")
    print(1,end=" ") 
if(len(list)>0):
    print(max+1,end=" ")
    print(start+1,end=" ")
    print(end+1,end=" ")
else:
    print(0)