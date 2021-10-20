def find_strings(play,ind_won,t_match,res,current_str,min):
    if(play==t_match):
        if(ind_won>=min):
            res.append(current_str)
        return
    find_strings(play+1,ind_won+1,t_match,res,current_str+'I',min)
    find_strings(play+1,ind_won,t_match,res,current_str+'A',min)

n=int(input())
min_wins_india_need=((n+1)//2 if n%2==1 else (n//2+1))
res=[]
find_strings(0,0,n,res,"",min_wins_india_need)
res.sort()
[print(i) for i in res]