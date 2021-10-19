#  class Node: 
  
#     # Constructor to initialize the node object 
#     def __init__(self, data): 
#         self.data = data 
#         self.next = None
  
# class LinkedList: 
  
#     # Function to initialize head 
#     def __init__(self): 
#         self.head = None
  
#     # Function to insert a new node at the beginning 
#     def push(self, new_data): 
#         new_node = Node(new_data) 
#         new_node.next = self.head 
#         self.head = new_node 
  
#     # Utility function to prit the linked LinkedList 
#     def printList(self): 
#         temp = self.head 
#         while(temp): 
#             print (temp.data, end=' ') 
#             temp = temp.next
  
#     def skipMdeleteN(self, M, N): 
#         if(M==0):
#             count3=0
#             temp3=self.head
#             while(count3!=N and temp3!=None):
#                 temp3=temp3.next
#                 count3+=1
#             self.head=temp3
#             return
#         count=1
#         temp=self.head
#         while(count!=M and temp!=None):
#             temp=temp.next
#             count+=1
#         new_ptr=temp
#         count2=0
#         while(count2!=N and new_ptr!=None):
#             count2+=1
#             new_ptr=new_ptr.next
#         # print(new_ptr.data)
#         if(new_ptr!=None):
#             temp.next=new_ptr.next
#         elif(temp!=None):
#             temp.next=None

          
  
# # Driver program to test above function 
  

# n = int(input())
# M,N = map(int, input().split())
# llist = LinkedList() 
# l = list(map(int, input().split()))
# l.reverse()
# for i in l:
#     llist.push(i)

# llist.skipMdeleteN(M, N) 
  
# llist.printList()


# Python program to delete M nodes after N nodes 
  
# Node class  
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to prit the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.data, end=' ') 
            temp = temp.next
  
    def skipMdeleteN(self, M, N):
        if(M==0):
            self.head=None
            return
        # Implment This 
        temp=self.head
        count=1
        while(True):
            f1=True
            f2=True
            
            while(count!=M and temp!=None):
                f1=False
                count+=1
                temp=temp.next
            count=0
            count2=0
            # print(temp.data)
            temp2=temp
            if(temp!=None):
                f2=False
                while(count2!=N and temp2!=None):
                    temp2=temp2.next
                    count2+=1
                    # print(temp2.data)
                if(temp2!=None):
                    # print(temp2.data)
                    temp.next=temp2.next
                else:
                    temp.next=temp2
            count2=0
            if(f1==True and f2==True):
                break
n = int(input())
M,N = map(int, input().split())
llist = LinkedList() 
l = list(map(int, input().split()))
l.reverse()
for i in l:
    llist.push(i)

llist.skipMdeleteN(M, N) 
  
llist.printList()