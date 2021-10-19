import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    ampm=s[len(s)-2]+s[len(s)-1]+""
    hour=s[0]+s[1]+""
    hour=int(hour)
    output=""
    if(ampm=="PM"):
        if(hour<12):
            hour+=12
    elif(ampm=="AM"):
        if(hour==12):
            hour="00"
        elif(hour<10):
            hour="0"+s[1]
    output+=str(hour)
    for i in range(2,len(s)-2):
        output+=s[i]
    print(output)
    return output
            
        
    
        

if __name__ == '__main__':
    s = input()

    result = timeConversion(s)
    print(result)

