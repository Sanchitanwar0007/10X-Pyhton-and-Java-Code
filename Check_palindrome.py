def checkPalindrome(str):
    arr=[]
    for i in range(len(str)):
        if(ord(str[i])>=65 and ord(str[i])<=90):
            ch=str[i].lower()
            arr.append(ch)
        if(ord(str[i])>=97 and ord(str[i])<=122):
            ch=str[i].lower()
            arr.append(ch)

    return is_palindrome(arr)
def is_palindrome(arr):
    i=0
    j=len(arr)-1
    while(i<j):
        if(arr[i]!=arr[j]):
            return False
        i+=1
        j-=1
    return True
n=int(input())
for i in range(n):
    str=input()
    print(checkPalindrome(str))