def valid(str,res,n):
    if(len(str)==n):
        res.append(str)
        return
    if(len(str)<2 or str[-1]!=str[-2]):
        valid(str+"a",res,n)
        valid(str+"b",res,n)
    elif(str[-1]=='a' and str[-2]=='a'):
        valid(str+"b",res,n)
    elif(str[-1]=='b' and str[-2]=='b'):
        valid(str+"a",res,n)
n=int(input())
res=[]
valid("",res,n)
[print(i) for i in res]
