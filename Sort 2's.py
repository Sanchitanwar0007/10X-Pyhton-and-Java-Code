n=int(input())
arr=list(map(int,input().split()))
sort_list=[]
for i in range(len(arr)):
    number=arr[i]
    temp=number
    count=0
    while(temp>0):
        m=temp%10
        # print(m)
        if(m==2):
            count+=1
        temp=temp//10
    sort_list.append([number,count])
    # print(number)
sort_list.sort(key= lambda x:x[0],reverse=True)
sort_list.sort(key=lambda x:x[1],reverse=True)
for i in range(len(sort_list)):
    print(sort_list[i][0],end=" ")