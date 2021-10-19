n,k=map(int,input().split())
arr=list(map(int,input().split()))
sum=0
for i in range(k):
    sum+=arr[i]
window=[]
window.append(sum)

for i in range(k,n):
    sum=sum+arr[i]-arr[i-k]
    window.append(sum)
print(min(window),max(window))