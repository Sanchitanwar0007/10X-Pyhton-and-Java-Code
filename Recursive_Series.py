def series(list,m,num):
    print(list)
    if(m==num):
        return list
    if(m%2==0):
        list.append(m-9)
        series(list,m+1,num)
    else:
        list.append(m-10)
        series(list,m+1,num)


n=int(input())
list=[]
for i in range(1,10):
    list.append(i)
print(list)
for i in range(n):
    num=int(input())
    m=10
    series(list,m,num)
    print(list)
    