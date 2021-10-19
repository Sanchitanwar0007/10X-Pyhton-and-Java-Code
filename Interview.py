n=int(input())
cand=[0]*n
talent=[0]*n
for i in range(n):
    c,t=map(int,input().split())
    cand[i]=c
    talent[i]=t
girl_list=[]
boy_list=[]
for i in range(len(cand)):
    if(cand[i]==0):
        girl_list.append(talent[i])
    else:
        boy_list.append(talent[i])

girl_list.sort(reverse=True)
boy_list.sort(reverse=True)
for i in range(len(girl_list)):
    print(girl_list[i],end=" ")
for i in range(len(boy_list)):
    print(boy_list[i],end=" ")

    
