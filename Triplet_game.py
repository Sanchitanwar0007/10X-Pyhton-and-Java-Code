a1,a2,a3=map(int,input().split())
b1,b2,b3=map(int,input().split())
alice=0
bob=0
if(a1>b1):
    alice+=1
if(b1>a1):
    bob+=1
if(a2>b2):
    alice+=1
if(a2<b2):
    bob+=1
if(a3>b3):
    alice+=1
if(a3<b3):
    bob+=1
print(alice,end=" ")
print(bob)
