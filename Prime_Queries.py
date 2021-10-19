import math
def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    prime[0]=False
    prime[1]=False

    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    prev=0
    arr=[0]*len(prime)
    for i in range(1,len(prime)):
        if(prime[i]==True):
            arr[i]=prev+1
            prev=arr[i]
        else:
            arr[i]=prev
    return arr

n,q=map(int,input().split())
arr=SieveOfEratosthenes(n)
for i in range(q):
    num=int(input())
    print(arr[num])
