def anagram(str1,str2):
    list1=[0]*256
    list2=[0]*256
    flag=0
    if(len(str1)==len(str2)):
        for i in range(len(str1)):
            list1[ord(str1[i])]+=1
            list2[ord(str2[i])]+=1
        for i in range(len(list1)):
            if(list1[i]==list2[i]):
                flag=1
            else:
                flag=0
                break
        if(flag==1):
            return 1
        else:
            return 0
    else:
        return 0


str1=input()
str2=input()
print(anagram(str1,str2))