from collections import Counter
n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
dict=Counter(arr[0])
for i in range(1,n):
    temp_dict=Counter(arr[i])
    for j in dict:
       if j in temp_dict:
           dict[j]=min(dict[j],temp_dict[j])
       else:
           dict[j]=-1
for k,v in sorted(dict.items()):
    if(v!=-1):
        print(k,v)

# gefgek
# gfgk
# kinfgg

