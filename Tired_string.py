string=input()
sum=0
for i in range(len(string)):
    sum+=ord(string[i])
if(sum%2==1):
    print("Yes")
else:
    print("No")