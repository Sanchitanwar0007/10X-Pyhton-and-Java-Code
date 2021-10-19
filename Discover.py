def find_k(l, k):
    # Implement this and return YES if found else return No
    left=0
    right=len(l)-1
    # print(l)
    while(left<=right):
        mid=(left+right)//2
        if(l[mid]==k):
            return "YES"
        elif(l[mid]<k):
            left=mid+1
        else:
            right=mid-1
    return "NO"
N,Q = input().split()
a = list(map(int,input().split(' ')))
a.sort() 
for i in range(int(Q)):
    k = int(input())
    print(find_k(a, k))