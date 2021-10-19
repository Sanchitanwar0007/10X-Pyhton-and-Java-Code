def game(r,g,b):
    list=[r,g,b]
    list.sort()
    count=0
    if(r==g and g==b):
        
        return r
    count+=list[1]
    temp=list[2]-list[1]
    if(temp%2==0):
        count+=temp//2
    else:
        count+=temp//2+1
    return count
for _ in range(int(input())):
    r,g,b=map(int,input().split())
    print(game(r,g,b))