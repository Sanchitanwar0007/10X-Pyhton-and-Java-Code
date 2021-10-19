def right_to_left_diagonal(list):
    diagonal=[]
    for i in range(len(list)):
        for j in range(len(list[0])):
            
            if((i+j)==len(list)-1):
                # val=i+j
                # print("I and J value",i,j,i+j)
                diagonal.append(list[i][j])
    return diagonal



# Do not change anything below this line
if __name__ == "__main__":
    m = int(input())
    lst = []    
    for val in range(0, m):
        lst.append([int(i) for i in input().split(' ')])
    out = right_to_left_diagonal(lst)
    # print(lst)
    [print(val) for val in out]