n=int(input())
for i in range(n):
    string=input()
    dictr={'r':0,'u':0,'b':0,'y':0}
    for i in range(len(string)):
        if(string[i]=='r'or string[i]=='u' or string[i]=='b' or string[i]=='y'):
            if string[i] in dictr:
                dictr[string[i]]+=1
    min=float('inf')
    for i in dictr:
        if(dictr[i]<min):
            min=dictr[i]
    print(min)
