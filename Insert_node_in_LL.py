# class Node: 
#     def __init__(self, value): 
#         self.data = value 
#         self.next = None
        
# class LinkedList: 
  
#     def __init__(self): 
#         self.head = None
  
#     def push(self, new_value): 
#         new_node = Node(new_value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return
#         self.tail.next = new_node
#         self.tail = new_node

#     def add_begin(self,head2,val):
#         new_node=Node(val)
#         if(head2 is None):
#             head2=new_node
#             return head2
#         new_node.next=head2
#         head2=new_node
#         return head2
#     def at_end(self,head2,val):
#         new_node2=Node(val)
#         if(head2 is None):
#             head2=new_node2
#             return head2
#         temp=head2
#         while(temp.next!=None):
#             temp=temp.next
#         # print(temp.data)
#         temp.next=new_node2
#         return head2
#     def makeListAndPrint(self):
#         #####WRITE CODE HERE####
#         head2=None
#         temp_val=self.head
#         temp_pos=self.head.next
#         while(temp_val!=None and temp_pos!=None):
#             val=temp_val.data
#             pos=temp_pos.data
#             # print(val,pos)
#             if(pos=='0'):
#                 head2=self.add_begin(head2,val)
#             if(pos=='1'):
#                 head2=self.at_end(head2,val)
#             temp_val=temp_val.next.next
#             if(temp_pos.next!=None):
#                 temp_pos=temp_pos.next.next
#         temp2=head2
#         while(temp2!=None):
#             print(temp2.data,end=" ")
#             temp2=temp2.next
#         return
            
        

# def read_list_input():
#     vals = input().split(' ')
#     linkedList = LinkedList() 
#     for val in vals:
#         linkedList.push(val)
#     return linkedList

# test_cases = int(input())
# for i in range(test_cases):
#     linkedList = read_list_input()
#     linkedList.makeListAndPrint()


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

    def add_begin(self,val):
        new_node=Node(val)
        if(self.head2 is None):
            self.head2=new_node
            return 
        new_node.next=self.head2
        self.head2=new_node
        
    def at_end(self,val):
        new_node2=Node(val)
        if(self.head2 is None):
            self.head2=new_node2
            return 
        temp=self.head2
        while(temp.next!=None):
            temp=temp.next
        # print(temp.data)
        temp.next=new_node2
        
    def makeListAndPrint(self):
        #####WRITE CODE HERE####
        self.head2=None
        temp_val=self.head
        temp_pos=self.head.next
        while(temp_val!=None and temp_pos!=None):
            val=temp_val.data
            pos=temp_pos.data
            # print(val,pos)
            if(pos=='0'):
                self.add_begin(val)
            if(pos=='1'):
                self.at_end(val)
            temp_val=temp_val.next.next
            if(temp_pos.next!=None):
                temp_pos=temp_pos.next.next
        temp2=self.head2
        while(temp2!=None):
            print(temp2.data,end=" ")
            temp2=temp2.next
        return
def read_list_input():
    vals = input().split(' ')
    linkedList = LinkedList() 
    for val in vals:
        linkedList.push(val)
    return linkedList

test_cases = int(input())
for i in range(test_cases):
    linkedList = read_list_input()
    linkedList.makeListAndPrint()