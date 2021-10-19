k=int(input())
s=input()
list=s.split(' ')
# print(list)
dict={}
for i in list:
    if(i in dict):
        dict[i]+=1
    else:
        dict[i]=1
ans=[]
print(dict)
for i in sorted(dict.keys()):
    if(dict[i]>k):
        ans.append(i)
if(len(ans)>0):
    for i in ans:
        print(i)
else:
    print("no such names in this town!!!")