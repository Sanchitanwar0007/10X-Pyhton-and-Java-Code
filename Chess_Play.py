def chess_Play(arr,i,j,m):
    if(i<0 or i>9 or j<0 or j>9):
        return 0
    if(m==0):
        if(arr[i][j]==0):  #Not visited to that place or visited first time
            arr[i][j]=1
            return 1
        else:
            return 0  # Already visited to that palace
    k=0
    k+=chess_Play(arr,i-2,j-1,m-1)
    k+=chess_Play(arr,i-2,j+1,m-1)
    k+=chess_Play(arr,i-1,j+2,m-1)
    k+=chess_Play(arr,i+1,j+2,m-1)
    k+=chess_Play(arr,i+2,j+1,m-1)
    k+=chess_Play(arr,i+2,j-1,m-1)
    k+=chess_Play(arr,i+1,j-2,m-1)
    k+=chess_Play(arr,i-1,j-2,m-1)
    return k
arr=[[0 for i in range(10)]for j in range(10)]
i,j,k=map(int,input().split())
print(chess_Play(arr,i-1,j-1,k))