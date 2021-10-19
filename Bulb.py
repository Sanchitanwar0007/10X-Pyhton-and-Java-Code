n=int(input())
# list=[]
count=0
prev='OFF'
for i in range(n):
    s=input()
    # list.append(s)
    if(i==0):
        if(s=='Toggle'):
            count+=1
            prev='ON'
        else:
            prev=s
    else:
        if(s=='Toggle' and prev=='OFF'):
            count+=1
            prev='ON'
        elif(s=='Toggle' and prev=='ON'):
            prev='OFF'
        elif(s=='ON' and prev=='OFF'):
            count+=1
            prev='ON'
        elif(s=='ON' and prev=='ON'):
            prev='ON'
        elif(s=='OFF'):
            prev='OFF'
print(count)
 #Got 100%
 