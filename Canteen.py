n,k=map(int,input().split())
arr=list(map(int,input().split()))
charge=int(input())
my_bill=0
for i in range(len(arr)):
    if(i!=k):
        my_bill+=arr[i]
total_bill=0
my_bill=my_bill//2
if(my_bill==charge):
    print("It is Correct!")
else:
    print(charge-my_bill)