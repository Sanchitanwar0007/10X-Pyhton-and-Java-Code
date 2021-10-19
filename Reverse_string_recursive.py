# your code goes here
# def reverse(string,len):
# 	if(len==0):
# 		print(string[len])
# 		return
# 	print(string[len],end="")
# 	reverse(string,len-1)
	
# n=int(input())
# for i in range(n):
#     string=input()
#     if(len(string)>0):
#         m=len(string)
#         reverse(string,m-1)


def reverse(string,len,s):
    if(len==0):
        return s+string[0]
    
    reverse(string,len-1,s)
    return s
n=int(input())
for i in range(n):
    string=input()
    num=len(string)
    # reverse(string,num-1,s="")
    print(reverse(string,num-1,s=""))