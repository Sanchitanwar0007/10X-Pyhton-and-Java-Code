class Node:
    def __init__(self,data:None,next:None):
        self.data=data
        self.next=next
def linked_list(head):
    temp=head
    while(temp!=None):
        print(temp.data,end="->")
        temp=temp.next
    # if(temp==None):
    #     print(None)
def insertHead(self,val):
    new_node=Node(val,None)
    new_node.next=self.head
    self.head=new_node
    # linked_list(head)
    # return head
def insert_in_between(head,pos,new_node):
    temp=head
    count=0
    while(temp!=None):
        if(count==pos-1):
            break
        count+=1
        temp=temp.next
    new_node.next=temp.next
    temp.next=new_node
    # linked_list(head)
def delete_node(head,pos):
    temp=head
    count=0
    while(count<pos-1):
        count+=1
        temp=temp.next
    temp.next=temp.next.next


head=Node(1,None)#  one Node
node2=Node(2,None)
head.next=node2
node3=Node(3,None)
node2.next=node3
insertHead(5)
linked_list(head)
# new_node2=Node(9,None)
# insert_in_between(head,2,new_node2)
# linked_list(head)
# delete_node(head,2)
# linked_list(head)

#head->......->None