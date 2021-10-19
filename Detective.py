# n=int(input())
# for i in range(n):
#     s1=input()
#     s2=input()
#     s1=s1.lower()
#     s2=s2.lower()
#     print(s1,s2)
#     d={}
#     for i in range(len(s1)):
#         if(s1[i] not in d):
#             d[s1[i]]=1
#         else:
#             d[s1[i]]+=1
#     flag=0
#     # print(d)
#     for i in range(len(s2)):
#         if((s2[i] in d) and dict[s2[i]]>0):
#             flag=1
#             d[s2[i]]=d[s2[i]]-1
#             # print(d)
#         else:
#             flag=0
#             break
#     if(flag==1):
#         print("YES")
#     else:
#         print("NO")



n=int(input())
for i in range(n):
    s1=input()
    s2=input()
    s1=s1.lower()
    s2=s2.lower()
    sett=set()
    for i in range(len(s1)):
        sett.add(s1[i])
    flag=0
    for i in range(len(s2)):
        if(s2[i] in sett):
            flag=1
        else:
            flag=0
            break
    if(flag==0):
        print("NO")
    else:
        print("YES")
