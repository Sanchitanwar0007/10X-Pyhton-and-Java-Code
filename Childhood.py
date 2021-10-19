swaps = int(input())
slist = [ ]
for i in range(swaps):
    m, n = input().split()
    slist.append([ m, n ])

string = input()

str_list = []
for i in range(len(string)):
    str_list.append(string[i])
# string=" ".join(str_list)
for i in slist:
    w1 = i [ 0 ]
    w3=i[0].lower()
    w2 = i [ 1 ]
    w4=i[1].lower()
    for i in range(len(str_list)):
        if (str_list[i]==w1):
            str_list[i]=w2
        elif(str_list[i]==w2):
            
            str_list[i]=w1
        elif(str_list[i]==w3):
            
            str_list[i]=w4
        elif(str_list[i]==w4):
            
            str_list[i]=w3
string="".join(str_list)
print(string)