# your code goes here
n=int(input())
for i in range(n):
    arr=list(map(int,input().split()))
    if(arr[1]<arr[3]):
        print("NO")
    else:
        count=0
        x1=arr[0]
        x2=arr[2]
        v1=arr[1]
        v2=arr[3]
        while(True):
            x1+=v1
            x2+=v2
            count+=1
            
            if(x1==x2):
                print("YES")
                break
            if(count>=9999999):
                print("NO")
                break

			
		
	