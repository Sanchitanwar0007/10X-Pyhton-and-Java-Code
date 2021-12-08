def print_recursive(n1,n2):
    if(n1>n2):
        return
    print(n1,end=" ")
    print_recursive(n1+1,n2)
for i in range(int(input())):
    start,end=map(int,input().split())
    print_recursive(start,end)
    print()