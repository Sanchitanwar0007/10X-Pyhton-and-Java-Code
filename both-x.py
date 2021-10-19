def bothCountX(string1, string2, x):
    # Complete this function, and return the list of resultant characters in sorted order
    string1=string1.lower()
    string2=string2.lower()
    dict={}
    dict2={}
    for i in string1: 
        if(i in dict):
            dict[i]+=1
        else:
            dict[i]=1
    for i in string2:
        if(i in dict2):
            dict2[i]+=1
        else:
            dict2[i]=1
    list=[]
    # print(dict,dict2)
    for i in sorted(dict):
        if i in dict2:
            if(dict[i]==x and dict2[i]==x):
                list.append(i)
    return list
		
for _ in range(int(input())):
    string1, string2, x = input().split()
    x = int(x)
    print(*bothCountX(string1, string2, x))