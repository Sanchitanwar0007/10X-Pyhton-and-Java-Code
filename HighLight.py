arr=list(map(int,input().split()))
string=input()
length=len(string)
arr2=[]
for i in range(len(string)):
    ch=string[i]
    arr2.append(arr[ord(ch)-97])
breadth=max(arr2)
print(length*breadth)