def gcd(num1,num2):
	while(num1!=num2):
		if(num1>num2):
			num1=num1-num2
		else:
			num2=num2-num1
	return num2
# def gcdByMod(n,m):
#     while(n!=0):
#         if(n>m):
#             n=n%m
#         else:
#             m=m%n
#     print(m)
n=int(input())
for i in range(n):
    n,m=map(int,input().split())
    hcf=gcd(n,m)
    print(hcf)