n=int(input())
for i in range(n):
    s=input()
	# if(s.find("hello")==-1):
	# 	print('No')
	# else:
	# 	print('Yes')
    s2='hello'
    j=0
    count=0
    for i in range(len(s)):
        if(s[i]==s2[j]):
            # count+=1
            j+=1
            if(j==len(s2)):
                break
        else:
            # count=0
            j=0
    if(j==len(s2)):
        print('Yes')
    else:
        print('No')