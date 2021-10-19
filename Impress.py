from sys import stdin,stdout
def Which_Day(arr, x):
# Implement This
    left=0
    right=len(arr)-1
    pos=-1
    while(left<=right):
        mid=(left+right)//2
        if(arr[mid]>=x):
            pos=mid
            right=mid-1
        if(arr[mid]>x):
            right=mid-1
        else:
            left=mid+1
    return pos
n,q = map(int,stdin.readline().split())
a = list(map(int,stdin.readline().split()))
for i in range(n):
    if i!=0:
        a[i] = a[i-1]+a[i]
k = list(map(int,stdin.readline().split()))
for i in range(q):
    ans = Which_Day(a,k[i])+1
    stdout.write(str(ans)+"\n")