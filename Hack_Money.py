def hack_Money(m):
    print(m)
    if(m==1 or m==0 or (m<10 and m%2==0)):
        return 'Yes'
    if(m%20==0):
        return hack_Money(m//10)
    elif(m%10==0):
        return hack_Money(m//10)
    return 'No'

n=int(input())
for i in range(n):
    num=int(input())
    if(num!=0):
        print(hack_Money(num))
    elif(num==0):
        print('No')
        
