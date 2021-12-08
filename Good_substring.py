d={0:-1}
n,c=map(int,input().split())
s=input()
k=-1
for i in range(len(s)):
    if(s[i]=='0'):
        k=k-1
    else:
        k=k+1
    d [ i + 1 ] = k
# print(d)
for i in range(c):
    m,l=map(int,input().split())
    if(d[m-1]==d[l]):
        print('yes')
    else:
        print('no')