def quickSort(arr,low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
def partition(arr,low,high):
    i = (low-1)         
    pivot = arr[high]    
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


n=int(input())
for i in range(n):
	arr=list(map(int,input().split()))
	if(len(arr)%2==0):    # If length of array is even 
		even=[0]*(len(arr)//2)
	else:                 # If length of array is even 
		even=[0]*((len(arr)//2)+1)
	odd=[0]*(len(arr)//2)   # Its same in case of odd and even 
	for i in range(len(arr)):
		if(i%2==0):
			even[i//2]=arr[i]    # we need to add elemnts in range of even length list else it will give List index out of bound
		else:
			odd[i//2]=arr[i]    # we need to add elemnts in range of even length list else it will give List index out of bound
	quickSort(even,0,len(even)-1)
	even.reverse()      # We must have to reverse the even elments because they need in decreasing order
	quickSort(odd,0,len(odd)-1)
	list1=[]
	if(len(arr)%2==0):
		for i in range(len(even)):
			list1.append(even[i])
			list1.append(odd[i])
	else:
		for i in range(len(odd)):
			list1.append(even[i])
			list1.append(odd[i])
		list1.append(even[len(even)-1])
	for i in range(len(list1)):
		print(list1[i],end=" ")
	print()