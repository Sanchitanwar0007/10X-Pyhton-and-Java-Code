def bestScore(A,B,C):
       # complete the function
       A.sort()
       B.sort()
       C.sort()
       i=0
       j=0
       k=0
       ans=float('inf')

       while(i<len(A) and j<len(B) and k<len(C)):
              list=[A[i],B[j],C[k]]   #|Tmax-Tmid|+|Tmin-Tmid|
              list.sort()
              ans=min(ans,(abs(list[2]-list[1])+abs(list[0]-list[1])))
              if(A[i]==min(list)):
                     i+=1
              elif(B[j]==min(list)):
                     j+=1
              else:
                     k+=1
       print(ans)


#DO not edit anything below this line

# Driver code 
A= [int(x) for x in input().split()] 
B= [int(x) for x in input().split()]  
C= [int(x) for x in input().split()]  
bestScore(A,B,C)



# 1 5 2 3
# 2 4 1 8
# 6 6 5 9