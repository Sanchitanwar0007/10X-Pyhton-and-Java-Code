from typing import Mapping


def selectionSort(arr, n):
    for i in range(len(arr)-1):
        min_ele=i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[min_ele]):
                min_ele=j
        temp=arr[min_ele]
        arr[min_ele]=arr[i]
        arr[i]=temp
    return arr
    

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(*selectionSort(arr, n))