def multiply(num):
    if(num<10):
       return num
    m=num%10
    return m*multiply(num//10)
n=int(input())
for i in range(n):
    num=int(input())
    if(num<0):
        num=-1*num
        print(multiply(num))
    else:
        print(multiply(num))