for _ in range(int(input())):
    x,y,q=map(int,input().split())
    x_set=set()
    y_set=set()
    x_set.add(1)
    y_set.add(1)
    x_set.add(x)
    y_set.add(y)
    for i in range(q):
        x1,y1=map(int,input().split())
        x_set.add(x1)
        y_set.add(y1)
    #for totaol partitions 
    # print(x_set)
    # print(y_set)
    print((len(x_set)-1)*(len(y_set)-1),end=" ")
    x_list=[]
    y_list=[]
    for i in x_set:
        x_list.append(i)
    for i in y_set:
        y_list.append(i)
    x_list.sort()
    y_list.sort()
    i=0
    j=1
    x_max=float('-inf')
    y_max=float('-inf')
    x_min=float('inf')
    y_min=float('inf')
    while(j<len(x_list)):
        temp=x_list[j]-x_list[i]
        if(temp<x_min):
            x_min=temp
        if(temp>x_max):
            x_max=temp
        i+=1
        j+=1
    # print(x_max,x_min)
    i=0
    j=1
    while(j<len(y_list)):
        temp=y_list[j]-y_list[i]
        if(temp<y_min):
            y_min=temp
        if(temp>y_max):
            y_max=temp
        i+=1
        j+=1
    print(x_min*y_min,end=" ")
    print(x_max*y_max)