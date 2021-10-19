def sumOfFirstN(n):
    if(n==0):
        print(0,0)
        return 0

    if(n==1):
        print(n,n)
        return n
    sum=n+sumOfFirstN(n-1)
    print(n,sum)
    return sum
# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    sumOfFirstN(n)