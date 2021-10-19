n,q=map(int,input().split())
str1=input()
str2=input()

for i in range(q):
    idx=int(input())-1
    s2=list(str2)
    for i in range(len(s2)):
        if(i==idx+1):
            break
        s2[i]="1"
    
    str2="".join(s2)
    print(str2)
    if(str2>=str1):
        print("YES")
    else:
        print("NO")

# # 5 5
# # 11111
# # 00010
# 1
# 2
# 3
# 4
# 5