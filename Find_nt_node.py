class Node: 
    def __init__(self, value): 
        self.data = value 
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
        
    def push(self, new_value): 
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node 
          
    def getNth(self, index): 
        ####WRITE CODE HERE###
        if(index==0):
        	return None
        ans=0
        count=1
        temp=self.head
        while(count<index):
        	count+=1
        	temp=temp.next
        if(temp==None):
        	return None
        return temp
        	

def read_list_input():
    vals = input().split(' ')
    linkedList = LinkedList() 
    for val in vals:
        linkedList.push(val)
    return linkedList

test_cases = int(input())
for i in range(test_cases):
    linkedList = read_list_input()
    index=int(input())
    print(linkedList.getNth(index))