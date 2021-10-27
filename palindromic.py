def substring(str):
    dp=[[False for i in range(len(str))] for j in range(len(str))]
    count=0
    for g in range(len(str)):
        i=0
        for j in range(g,len(str)):
            if(g==0):
                dp[i][j]=True
            elif(g==1):
                if(str[i]==str[j]):
                    dp[i][j]=True
            else:
                if(str[i]==str[j] and dp[i+1][j-1]==True):
                    dp[i][j]=True
            if(dp[i][j]==True):
                count+=1
            i+=1
    
    return count
            

for i in range(int(input())):
    str=input()
    # print(is_palindrome(str))
    print(substring(str))
