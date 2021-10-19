list=list(map(int,input().split()))
n=len(list)
count=1
list.sort()
sum=0
nth=[]
for i in range(n-1):
    if(list[i]==list[i+1]):
	    count+=1
    else:
        nth.append(count)
        count=1
if(count>1):
    nth.append(count)
# print(nth)
for i in nth:
    # print("Sum =>",sum)
    sum+=((i-1)*(i))//2
print(sum)


# It is )=O(nlogn) solution we can do it in O(n) using dictionary



        
        