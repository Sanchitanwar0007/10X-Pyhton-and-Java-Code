n=int(input())
for i in range(n):
    num=int(input())
    list1=list(map(int,input().split()))
    index=-1
    if(len(list1)==1):
        print(1)
        continue
    if(list1[0]>list1[1]):
        index=1
    if(index==-1):
        for i in range(len(list1)-1):
            if(list1[i]>list1[i-1] and list1[i]>list1[i+1]):
                index=i+1
                break
    if(list1[len(list1)-1]>list1[len(list1)-2] and index==-1):
        index=len(list1)
    print(index)