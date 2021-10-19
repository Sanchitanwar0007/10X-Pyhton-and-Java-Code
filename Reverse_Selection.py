def reverseSelectionSort(A, n):
    for i in range(n):
        mini=arr[i]
        idx=i
        for j in range(i+1,n):
            if(mini<arr[j]):
                mini=arr[j]
                idx=j
        arr[i],arr[idx]=arr[idx],arr[i]
    return arr

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(*reverseSelectionSort(arr, n))