def intToArr(N):
    #complete this function
    list=[]
   
    while(N>0):
    	n=N%10
    	list.append(n)
    	N=N//10
    list.reverse()
    return list

def remove_3(arr):
    #complete this function
    remove=[]
    for i in range(len(arr)):
        if(arr[i]!=3):
            remove.append(arr[i])
    return remove
def arrToInt(arr):
    #complete this function
    sum=arr[0]
    for i in range(1,len(arr)):
        sum=sum*10+arr[i]
    return sum
#DO NOT change anything below this line

N=int(input())
arrNum=intToArr(N)
arrNumWithout3=remove_3(arrNum)
print(arrToInt(arrNumWithout3))