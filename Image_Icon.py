n=int(input())
img=[]
for i in range(n):
    img.append(int(input()))
m=int(input())
icon=[]
for i in range(m):
    icon.append(int(input()))
if m==0:
    print(0)
else:
    count=0
    for i in range(n-m+1):
        pixel=img[i:i+m]
        #print(pixel)
        if pixel==icon:
            count+=1
    print(count)