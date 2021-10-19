for _ in range(int(input())):
    s=input()
    arr=[]
    for i in range(len(s)):
        arr.append(s[i])
    code_arr=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    code_arr.reverse()
    dict={}
    string=""
    for i in range(len(arr)):
        if(arr[i]!=" "):
            code_idx=122-ord(arr[i])
            string+=code_arr[code_idx]
        else:
            if string not in dict:
                dict[string]=1
            else:
                dict[string]+=1
            string=""
        # print(string)
    if(string!=""):
        if string not in dict:
                dict[string]=1
        else:
            dict[string]+=1 #--...-
    ans=0
    # print(dict)
    for i in dict:
        ans+=1
    print(ans)