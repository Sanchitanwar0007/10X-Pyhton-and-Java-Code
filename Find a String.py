def count_substring(string, sub_string):
    i=0
    j=0
    count=0
    while(i<len(string)):
        # print("i")
        if(string[i]==sub_string[j]):
            j+=1
            # print("j",j)
            if(j==len(sub_string)):
                i-=1
                j=0
                
                count+=1
        else:
            j=0
        i+=1   
    return count  
string=input()
substring=input()
count=count_substring(string, substring)
print(count)