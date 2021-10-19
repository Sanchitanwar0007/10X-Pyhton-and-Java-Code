def max_agents(arr):
    dic={}
    for i in range(len(arr)):
        string=arr[i]
        strr=sorted(string)
        string="".join(strr)
        if(string in dic):
            dic[string]+=1
        else:
            dic[string]=1
    max=-1
    # print(dic)
    for i in dic:
        if(max<dic[i]):
            max=dic[i]
    return max
n=int(input())
arr=list(input().split())
maxx=max_agents(arr)
print(maxx) 