n=int(input())
dict={}
dict['football']=0
name_dict={}
for i in range(n):
    name,sport=input().split()
    if(name not in name_dict):
        name_dict[name]=True
        if sport in dict:
            dict[sport]+=1
        else:
	        dict[sport]=1
maxx=max(dict.values())

for i in sorted(dict.keys()):
    if dict[i]==maxx:
        print(i)
        break
print(dict['football'])


# 7
# abir cricket
# aayush cricket
# newton kabaddi
# abhinash badminton
# sanjay tennis
# abhinash badminton
# govind football