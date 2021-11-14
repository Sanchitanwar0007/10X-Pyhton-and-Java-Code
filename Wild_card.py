def all_com(s,start,total,ans,ch):
    if(ch==len(s)):
        if(total==start):
            print(ans)
        return
    if(s[ch]=='?'):
        all_com(s,start+1,total,ans+"0",ch+1)
        all_com(s,start+1,total,ans+"1",ch+1)
    else:
        all_com(s,start,total,ans+s[ch],ch+1)

s=input()
total=0
for i in range(len(s)):
    if(s[i]=='?'):
        total+=1
if(total==0):
    print(s)
else:
    all_com(s,0,total,"",0)
