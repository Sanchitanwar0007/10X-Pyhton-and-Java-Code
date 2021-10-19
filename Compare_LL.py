class Node:
    def __init__(self, nodeValue):
        self.data = nodeValue
        self.next = None

#do not change anything above This
def Compare(list1 ,list2):
    temp1=list1
    temp2=list2
    data1=0
    data2=0
    while(temp1!=None and temp2!=None):
        data1=data1*10+temp1.data
        data2=data2*10+temp2.data
        temp1=temp1.next
        temp2=temp2.next
    if(temp1!=None):
        while(temp1!=None):
            data1=data1*10+temp1.data
            temp1=temp1.next
    if(temp2!=None):
        while(temp2!=None):
            data2=data2*10+temp2.data
            temp2=temp2.next
    if(data1>data2):
        return 1
    elif(data1<data2):
        return -1
    else:
        return 0
def buildListFromArray(givenArray):

    numElements = len(givenArray)
    if numElements == 0:
        return None
    head = Node(givenArray[0])
    prevNode = head
    for index in range(1, numElements):
        newNode = Node(givenArray[index])
        prevNode.next = newNode
        prevNode = newNode
    return head

if __name__ == '__main__':

    numTest = int(input())

    for i in range(numTest):

        n, m = map(int, input().split())

        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))

        head1, head2 = buildListFromArray(arr1), buildListFromArray(arr2)


        flag = Compare(head1, head2)

        print(flag)