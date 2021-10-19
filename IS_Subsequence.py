def isSubsequence(s,string):
    i=0
    j=0
    if(len(s)<len(string)):
        return False
    while(i<len(s) and j<len(string)):
        if(s[i]==string[j]):
            j+=1
        i+=1
    if(j==len(string)):
        return True
    else:
        return False
def hackerrankInString(s):
    string="hackerrank"
    if(isSubsequence(s,string)):
        return 'YES'
    else:
        return 'NO'
s=input()
print(hackerrankInString(s))

