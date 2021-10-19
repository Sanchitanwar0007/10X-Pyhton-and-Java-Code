for _ in range(int(input())):
    s1,s2=input().split()
    s=sorted(s2)
    s3=sorted(s1)
    s1="".join(s3)
    s2="".join(s)
    if(s1==s2):
        print(True)
    else:
        print(False)