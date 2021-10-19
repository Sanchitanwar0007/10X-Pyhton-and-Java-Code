for _ in range(int(input())):
    s=input()
    arr=list(s)
    arr.sort()
    s1=""
    s2=""
    for i in range(len(arr)):
        if(i%2==0):
            s1+=arr[i]
        else:
            s2+=arr[i]
    for i in range(len(s2)-1,-1,-1):
        s1+=s2[i]
    print(s1)
    

