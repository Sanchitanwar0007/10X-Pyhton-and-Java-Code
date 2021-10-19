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

    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data, end=" ")
            temp = temp.next

# Do not change anything above this line
    def reverse(self,slow):
        prev=None
        cur=slow
        while(cur!=None):
            temp2=cur.next
            cur.next=prev
            prev=cur
            cur=temp2
        return prev
    def reorderList(self):
        # YOU ONLY NEED TO COMPLETE THIS FUNCTION.
        slow=self.head
        fast=self.head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        # print(slow.data)
        head1=self.head
        head2=slow.next
        slow.next=None
        head2=self.reverse(head2)
        curr=Node(0)
        t=curr
        while(head1!=None or head2!=None):
            if(head1!=None):
                curr.next=head1
                curr=curr.next
                head1=head1.next
            if(head2!=None):
                curr.next=head2
                curr=curr.next
                head2=head2.next
        return t.next
# Do not change anything below this line
if __name__ == '__main__':
    
    n = int(input())

    # Start with the empty list 
    llist = LinkedList() 

    temp = [int(x) for x in input().split()]

    if(n<1):
        llist.head = None
    elif(n<2):
        llist.head = Node(temp[0])
    else:
        llist.head = Node(temp[0])
        second = Node(temp[1])
        llist.head.next = second
        curr = llist.head.next


    for i in range(2,n):
        t = Node(temp[i])
        curr.next = t
        curr = curr.next

    llist.head = llist.reorderList()
    llist.printList()