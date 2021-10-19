for _ in range(int(input())):
    s=input()
    dict={}
    for i in range(len(s)):
        if(s[i] not in dict):
            dict[s[i]]=1
        else:
            dict[s[i]]+=1
    
    idx=-1
    for i in range(len(s)):
        if(dict[s[i]]==1):
            idx=i
            break
    if(idx==-1):
        print(idx)
    else:
        print(idx)
