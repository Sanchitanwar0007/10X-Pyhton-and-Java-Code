# n,m=map(int,input().split())
# arr=[]
# for i in range(n):
#     arr.append(input())

# str_to_char=[]
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         s=arr[i]
#         str_to_char.append(s[j])

# temp=[]
# j=0
# for i in range(m):
#     string=""
#     prev=j
#     while(j<len(str_to_char)):
#         string+=str_to_char[j]
#         j+=m
#     j=prev+1
#     temp.append(string)
# count=0
# for i in range(len(temp)):
#     col_str=temp[i]
#     new_str=sorted(temp[i])
#     fin_string="".join(new_str)
#     # print(col_str,fin_string)
#     if(col_str!=fin_string):
#         count+=1
# print(count)



n,k=map(int, input().split())
a=[]
for i in range(n):
    s=input()
    s=list(s)
    # print(s)
    a.append(s)
print(a)
c=0
for i in range(k):
    q=[]
    for j in range(n):
        q.append(a[j][i])
    print(q)
    for k in range(n-1):
        if q[k] > q[k+1]:
            c+=1
            break
print(c)