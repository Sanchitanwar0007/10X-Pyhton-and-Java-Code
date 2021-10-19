def gcd(num1,num2):
    if(num2==0):
        return num1
    return gcd(num2,num1%num2)
for _ in range(int(input())):
    num1,num2=map(int,input().split())
    print(gcd(num1,num2))