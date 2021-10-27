def row_column(arr):
    
    for i in range(len(arr)):
        row=set()
        for j in range(len(arr)):
            if(arr[i][j] in row and arr[i][j].isdigit()):
                return False
            elif(arr[i][j].isdigit()):
                row.add(arr[i][j])
    
    for i in range(len(arr)):
        col=set()
        for j in range(len(arr)):
            if(arr[j][i] in col and arr[j][i].isdigit()):
                return False
            elif(arr[j][i].isdigit()):
                col.add(arr[j][i])
    # for k in range(len(arr)):
    #     if(k+2<len(arr)):
    #         for i in range(k,k+3):
    #             met=set()
    #             for j in range(k,k+3):
    #                 if(arr[i][j].isdigit and arr[i][j] in met):
    #                     return False
    #                 elif(arr[i][j].isdigit):
    #                     met.add(arr[i][j])
    #     k+=3
    return True

arr=[]
for i in range(9):
    arr.append(input().split())
print(row_column(arr))
