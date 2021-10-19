n=int(input())
arr=list(map(int,input().split()))
arr.sort()
arr.reverse()
num1=""
num2=""
for i in range(len(arr)):
    if(i%2==0):
        num1+=str(arr[i])+""
    else:
        num2+=str(arr[i])+""
num1=int(num1)
num2=int(num2)
print(num1+num2)
