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
    def reverse_half(self):
        prev=self.head
        curr=self.head.next
        while(curr!=None and curr.next!=None):
            prev=prev.next
            curr=curr.next.next
        
        node=None
        temp=prev.next

        while(temp!=None):
            temp2=temp.next
            temp.next=node
            node=temp
            temp=temp2
        prev.next=node

    def isPalin(self):
        self.reverse_half()
        temp=self.head
        prev=self.head
        curr=self.head.next
        while(curr!=None and curr.next!=None):
            prev=prev.next
            curr=curr.next.next
        prev=prev.next
        while(prev!=None):
            # print(temp.data,prev.data)
            if(prev.data!=temp.data):
                return False
            prev=prev.next
            temp=temp.next
        return True
def read_list_input():
    vals = input().split(' ')
    linkedList = LinkedList() 
    for val in vals:
        linkedList.push(val)
    return linkedList

test_cases = int(input())
for i in range(test_cases):
    linkedList = read_list_input()
    print(linkedList.isPalin())