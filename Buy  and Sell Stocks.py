n=int(input())
list=[]
for i in range(n):
    list.append(int(input()))
max_profit=0
min=float('inf')
for i in range(len(list)):
    if(min>list[i]):
        min=list[i]
    each_day=list[i]-min
    if(max_profit<each_day):
        max_profit=each_day
print(max_profit)
