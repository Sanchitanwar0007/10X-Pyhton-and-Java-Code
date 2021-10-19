# Complete this addStrings() function

def addStrings(num1, num2):     
    if(len(num1)<len(num2)):
        num1,num2=num2,num1
    j=len(num2)-1
    res=""
    carry=0
    for i in range(len(num1)-1,-1,-1):
        n1=ord(num1[i])-48
        if(j>=0):
            n2=ord(num2[j])-48
            temp=n1+n2+carry
        else:
            temp=n1+carry
        if(temp>=10):
            carry=temp//10
            temp=temp%10
        else:
            carry=0
        res+=str(temp)+""
        j-=1
    if(carry>0):
        res+=str(carry)+""
    ans=""
    for i in range(len(res)-1,-1,-1):
        ans+=res[i]+""
    return ans


for _ in range(int(input())):
    n1, n2 = input().split()
    print(addStrings(n1,n2))