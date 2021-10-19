n=int(input())
list=[]
for i in range(n):
    num=int(input())
    prev=num
    if(num<38):
        print(num)
        continue
    elif(num>=38):
        while(num%5!=0):
            num+=1
    if(num-prev<3):
        print(num)
    else:
        print(prev)