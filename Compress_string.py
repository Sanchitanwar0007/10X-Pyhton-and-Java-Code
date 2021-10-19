def compress(s):
    count=1
    str1=""
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            count+=1
        else:
            if(count>1):
                str1+=s[i]+str(count)+""
                count=1
            else:
                str1+=s[i]+""
                count=1
    if(count>1):
        str1+=s[len(s)-1]+str(count)+""
    else:
        str1+=s[len(s)-1]+""
    print(str1)
       ### Complete this function.

t = int(input())
for _ in range(t):
    st = input()
    compress(st)