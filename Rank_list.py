# list=[]
# for _ in range(int(input())):
#     n,s,m=input().split()
#     list.append((n,int(s),int(m)))
# print(list)
# list.sort()
# print(list)

# 5
# b 10 30
# a 10 30
# a 11 30
# b 11 30
# c 11 29
val=[]
for i in range(int(input())):
    a,b,c=map(str,input().split())
    b=int(b)
    c=int(c)
    val.append((a,b,c))
val.sort(key=lambda x:x[1])
val.sort(key=lambda x:x[0])
val.sort(key=lambda x:x[2],reverse=True)

[print(*i) for i in val]
