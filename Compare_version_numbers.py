def compare(l1,l2):
    if l1==l2:
        return 0
    n1,n2=len(l1),len(l2)
    if n1>n2:
        for i in range(n1-n2):
            l2.append('0')
    if n2<n1:
        for i in range(n2-n1):
            l1.append('0')
    for i in range(len(l1)):
        if int(l1[i])>int(l2[i]):
            return(1)
        elif int(l1[i])<int(l2[i]):
            return(-1)
    return 0
for _ in range(int(input())):
    s1,s2=map(str,input().split())
    l1=list(map(int,s1.split('.')))
    l2=list(map(int,s2.split('.')))
    print(compare(l1,l2))