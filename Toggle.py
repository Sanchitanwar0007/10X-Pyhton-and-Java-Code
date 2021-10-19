def convert(string):
    temp=""
    for i in range(len(string)):
        if(ord(string[i])>96 and ord(string[i])<123):
            # print("yes")
            s=string[i].upper()
            temp+=s+""
        else:
            temp+=string[i].lower()+""
    
    print(temp)
string=input()
convert(string)