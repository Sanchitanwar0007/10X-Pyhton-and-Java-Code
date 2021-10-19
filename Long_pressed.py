def isSubstring(name, type):
    i=0
    j=0
    while(i<len(name) and j<len(type)):
        if(name[i]==type[j]):
            i+=1
            j+=1
        else:
            j+=1
    if(i==len(name)):
        return True
    else:
        return False

for _ in range(int(input())):
    name,type=input().split()
    print(isSubstring(name,type))