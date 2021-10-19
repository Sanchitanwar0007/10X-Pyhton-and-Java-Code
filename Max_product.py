# n=int(input())
# max_product=float('-inf')
# for i in range(n):
# 	num=int(input())
# 	if(i==0):
# 		prev=num
# 	elif((prev*num)>max_product):
# 		max_product=prev*num
# 	prev=num
# print(max_product)
# 		# Overall Space complexity is O(1) and time complexity is O(n)

n = int(input())
lst = []
for i in range(n):
	num = int(input())
	lst.append(num)
product =float('-inf')
for i in range(len(lst)-1):
	if (lst[i]*lst[i+1]>product):
		product=lst[i]*lst[i+1]
print(product)