def transpose_matrix(list):
    r=len(list)
    c=len(list[0])
    # print(r,c)
    arr=[[0 for i in range(r)] for j in range(c)]
    for i in range(len(list[0])):
        for j in range(len(list)):
            arr[i][j]=list[j][i]
    return arr

# do not change anything below this line
if __name__ == "__main__":
    h = int(input())
    lst = []
    for val in range(0, h):
        lst.append([int(i) for i in input().split(' ')])
    out = transpose_matrix(lst)
    for val in out:
        print(" ".join(str(i) for i in val))