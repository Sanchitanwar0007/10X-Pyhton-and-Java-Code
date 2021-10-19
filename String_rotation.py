def isSubstring(s1, s2):
    if s1.find(s2) != -1:
        return True
    if s2.find(s1) != -1:
        return True
    return False

def isRotation(s1,s2):
    if(len(s1)<len(s2)):
        print(False)
        return False
    temp=s1.strip()+s1
    # print(s2,temp)
    if(isSubstring(temp,s2.strip())):
        print(True)
        return True
    else:
        print(False)
        return False

t = int(input()) 
for i in range(t):
    s1 = input() 
    s2 = input()
    isRotation(s1,s2)
    # print(isSubstring(s1,s2))

