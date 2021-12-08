pattern=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
n=int(input())
for i in range(n):
    msg=input()
    sett=set()
    temp=""
    for i in range(len(msg)):
        ch=msg[i]
        if(ch!=' '):
            arr_idx=ord(ch)-97
            temp+=pattern[arr_idx]
        else:
            sett.add(temp)
            temp=""
        # print(temp)
    if(len(temp)>0):
        sett.add(temp)
    print((len(sett)))
            