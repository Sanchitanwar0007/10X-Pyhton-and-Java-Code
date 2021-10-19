def calSumUtil( A , B , n , m ): 
   # Implement this 
   # A is the first array
   # n is size of array A
   # B is the second array
   # m is size of array B
    n1=0
    n2=0
    for i in range(n):
        n1=n1*10+A[i]
    for i in range(m):
        n2=n2*10+B[i]
    add=n1+n2
    arr=[]
    while(add>0):
        arr.append(add%10)
        add=add//10
    arr.reverse()
    return arr


# Wrapper Function 
def calSum(a, b, n, m ): 
  
    # Making first array which have 
    # greater number of element
    # A is the first array
    # n is size of array A
    # B is the second array
    # m is size of array B 
    if n >= m: 
        return calSumUtil(a, b, n, m) 
    else: 
        return calSumUtil(b, a, m, n) 
  
# Driven Code 
testCase = int(input())
for _ in range(testCase):
	A = list(map(int,input().split()))
	B = list(map(int,input().split()))
	res = calSum(A, B, len(A), len(B))
	print(*res)