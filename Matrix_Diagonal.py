def change_diagonal(list):
	
	for i in range(len(list)):
		for j in range(len(list[0])):
			if(i==j):
				if(list[i][j]>=0):
					list[i][j]=1
				else:
					list[i][j]=0
	return list
# Do not change anything below this line.
if __name__ == "__main__":
    val = int(input())
    lst = []
    for index in range(0, val):
        lst.append([int(i) for i in input().split(' ')])
    out = change_diagonal(lst)
    for lst1 in out:
        print(" ".join(str(i) for i in lst1))