n=int(input())
tower=input()
bulbs=int(input())
max_bt=0
count=1
for i in range(len(tower)-1):
    if(tower[i]=='O'):
        if(tower[i]==tower[i+1]):
            count+=1
        else:
            max_bt=max(max_bt,count)
            count=1
print(count)