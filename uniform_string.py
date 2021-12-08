n=int(input())
string=input()
dictionary={}

for i in range(len(string)):
    if(string[i] in dictionary):
        dictionary[string[i]]+=1
    else:
        dictionary[string[i]]=1
# print(dictionary)
d={}
for i in dictionary:
    if(dictionary[i] in d):
        d[dictionary[i]]+=1
    else:
        d[dictionary[i]]=1
arr=[]
for i in d:
    arr.append(d[i])
maxi=max(arr)
check=0
for i in range(len(arr)):
    if(arr[i]>1 and arr[i]!=maxi):
        check=1
if(check==0):
    print("True")
else:
    print("False")
