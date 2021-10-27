class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None

 # DO NOT CHANGE ANYTHING ABOVE THIS LINE

    # Function to reverse a Doubly Linked List
    def reverse(self):
        temp=self.head
        curr=None
        while(temp!=None):
            curr=temp.prev
            temp.prev=temp.next
            temp.next=curr
            temp=temp.prev
            
        if(curr!=None):
            self.head=curr.prev


 # DO NOT CHANGE ANYTHING BELOW THIS LINE

    # Given a reference to the head of a list and an
    # integer,inserts a new node on the front of list

    def push(self, new_data):

        # 1. Allocates node
        # 2. Put the data in it
        new_node = Node(new_data)

        # 3. Make next of new node as head and
        # previous as None (already None)
        new_node.next = self.head

        # 4. change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node

        # 5. move the head to point to the new node
        self.head = new_node

    def printList(self, node):
        while(node is not None):
            print(node.data, end=' ')
            node = node.next


# Driver code
for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]

    dll = DoublyLinkedList()
    for idx in range(len(arr)-1, -1, -1):
        dll.push(arr[idx])

    dll.reverse()
    dll.printList(dll.head)
    print()
