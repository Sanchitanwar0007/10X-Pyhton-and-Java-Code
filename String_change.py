s1=input()
s2=input()
n=0
m=0

for i in range(len(s1)):
	 n+=ord(s1[i])
for i in range(len(s2)):
    m+=ord(s2[i])
if(m==n):
    print(1)
else:
    print(0)



