# def swap(arr):
#     maxi=float("-inf")
#     mini=float("inf")
#     max_index=-1
#     min_index=-1
#     for i in range(len(arr)):
#         if(arr[i]>maxi):
#             maxi=arr[i]
#             max_index=i
#         if(arr[i]<mini):
#             mini=arr[i]
#             min_index=i
#     arr[max_index]=mini
#     arr[min_index]=maxi
#     print(*arr)
# for _ in range(int(input())):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     swap(arr)

def selectSwap(arr, n):
    maxi=float("-inf")
    mini=float("inf")
    max_index=-1
    min_index=-1
    for i in range(len(arr)):
        if(arr[i]>maxi):
            maxi=arr[i]
            max_index=i
        if(arr[i]<mini):
            mini=arr[i]
            min_index=i
    arr[max_index]=mini
    arr[min_index]=maxi
    return arr

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(*selectSwap(arr, n))