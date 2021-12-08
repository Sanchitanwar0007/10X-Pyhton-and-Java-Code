n=int(input())
car=list(map(int,input().split()))
bus=list(map(int,input().split()))
min_cost=0
val=False
for i in range(n):
    if(car[i]<=bus[i]):
        min_cost+=car[i]

    else:
        min_cost+=bus[i]
        val=True
print(min_cost)