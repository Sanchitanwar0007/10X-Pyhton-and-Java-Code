def palindrome(string,num):
	st=string+""
	if(num==0):
		st+=string[::-1]+""
	elif(num==1):
		rev=string[::-1]
		#print(rev)
		for i in range(1,len(rev)):
			st+=rev[i]+""
	return st
	

s=input()
n=int(input())
if(len(s)==1):
	print(s)
else:
	print(palindrome(s,n))