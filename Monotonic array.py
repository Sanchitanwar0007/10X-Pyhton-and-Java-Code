n=int(input())
count=0
dcount=0
for i in range(n):
    num=int(input())
    if(i==0):
        count+=1
        dcount+=1
        prev=num
    if(i>0):
        if(num>prev):
            count+=1
            prev=num
            if(dcount>1):
                print(False)
                break
        elif(num==prev):
            if(count>1):
                count+=1
            else:
                dcount+=1
        else:
            if(count>1):
                print(False)
                break
            dcount+=1
            prev=num
if(dcount==n):
    print(True)
elif(count==n):
    print(True)
            

