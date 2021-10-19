def stringInsertionSort(str):
    # Your code goes here
    list=[]
    for i in range(len(str)):
        list.append(str[i])
    for i in range(len(str)):
    	j=i
    	while j>0 and ord(list[j])<ord(list[j-1]):
    		list[j],list[j-1]=list[j-1],list[j]
    		j-=1
    s=""
    for i in list:
        s+=i+""
    return s

### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__=='__main__':
    input_string = input()
    print(stringInsertionSort(input_string))