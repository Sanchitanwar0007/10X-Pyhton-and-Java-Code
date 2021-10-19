n,m=map(int,input().split())
string=input()
for i in range(m):
    i,j=map(int,input())
    i=i-1
    j=j-1
    count_0=0
    count_1=0
    for i in range(i,j):
        if(string[i]=='0'):
            
