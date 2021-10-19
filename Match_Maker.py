n=int(input())
for i in range(n):
    num=int(input())
    boys=list(map(int,input().split()))
    girls=list(map(int,input().split()))
    girls.sort()
    boys.sort(reverse=True)
    count=0
    for i in range(num):
        if(girls[i]%boys[i]==0 or boys[i]%girls[i]==0):
            count+=1
    print(count)