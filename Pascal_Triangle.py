import math
# In pascal triangle each and every step sum is in 2^n for ex: 1st line sum 2^0 is 1 and 2nd line sum is 2^1 i.e 2 and so on
n=int(input())
list=[]
p=n-1
for i in range(p+1):
    fact=math.factorial(p)
    
    l_fact=math.factorial(i)
    
    b_fact=math.factorial(p-i)
    num=fact//(b_fact*l_fact)
    list.append(num)
for i in range(len(list)):
    print(list[i])