def binary_string(n,ans,limit,res):
    if(limit==n):
        print(ans,end=" ")
        return
    binary_string(n,ans+"0",limit+1,1)
    if(limit==0):
        binary_string(n,ans+"1",limit+1,0)
    elif(res==1):
        binary_string(n,ans+"1",limit+1,0)
n=int(input())
binary_string(n,"",0,0)
