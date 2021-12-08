def mean(arr, arr_size):
    # Complete this function
    summ=sum(arr)
    return summ//arr_size

def median(arr, arr_size):
    arr.sort()
    # Complete this function
    if(arr_size%2==0):
        arr.sort()
        # print(arr[len(arr)//2],arr[(len(arr)//2)-1])
        med=arr[len(arr)//2]+arr[(len(arr)//2)-1]
        return med//2
    else:
        return arr[len(arr)//2]
### DO NOT CHANGE ANYTHING BELOW THIS LINE

for _ in range(int(input())):
    length = int(input())
    arr = [int(x) for x in input().split()]
    print(mean(arr, length) , median(arr, length))