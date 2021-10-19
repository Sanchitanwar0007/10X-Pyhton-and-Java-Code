def gcd(a,b):
    if(a==0):
        return b
    return gcd(b%a,a)
def lcm(a,b):
    return a//gcd(a,b)*b
n=int(input())
arr=list(map(int,input().split()))
res=arr[0]
for i in range(1,len(arr)):  #lcm=a*b/gcd(a,b)
    res=lcm(res,arr[i])
print(res)

