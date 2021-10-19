def last_one(p,q):
    if(p==q or q==0):
        print(1)
        return
    if(q>p):
        print(1)
        return
    if(q==1):
        print(1)
        return
    arr=[]
    for i in range(p):
        arr.append(i+1)
    # print(arr)
    while(True):
        temp=[]
        i=0
        while(i<(len(arr))):
            if((i+1)%q==0 and i!=0):
                temp.append(arr[i])
            i+=1
        # print(temp)
        arr=temp
        if(len(arr)<q):
            break
    print(arr[0])
n=int(input())
for i in range(n):
    p,q=map(int,input().split())
    last_one(p,q)
# O(N) appproch for Your Intership

    # for _ in range(int(input())):
	# l,k=map(int,input().split())
	# # print(l,k)
	# n=int(l/k)
	# v=k
	# if(l<k):
	# 	print(1)
	# 	continue
	# while(n>=k):
	# 	v=v*k
	# 	n=int(l/v)
	# print(v)