t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    dict={}
    sum=0
    for i in range(n):
        if s[i] in dict:
            dict[s[i]]+=1
        else:
            dict[s[i]]=0
        sum+=dict[s[i]]
    print(sum)