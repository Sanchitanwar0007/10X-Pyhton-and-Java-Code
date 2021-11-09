def total_number(n,ans,list,rem):
    if(n==len(ans)):
        if(rem==0):
            list.append(ans)
        return
    total_number(n,ans+"L",list,rem+1)
    total_number(n,ans+"R",list,rem-1)
    total_number(n,ans+"S",list,rem)

n=int(input())
list=[]
total_number(n,"",list,0)
print(list)
