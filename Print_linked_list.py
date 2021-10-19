class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


class LL:
    def __init__(self):
        self.head = None
    
    	
    #complete the Display function given below
    
    def display(self):
        print("head->",end="")
        while(self.head!=None):
            print(self.head.data,end='->')
            self.head=self.head.next
            if(self.head==None):
                print("None")
    @staticmethod
    def insert_node(val, current):
        temp = Node(val)
        current.next = temp
        current = current.next
        return current


ll = LL()
num = [int(i) for i in input().split("->")]
ll.head = Node(num[0])
curr = ll.head
for i in num[1:]:
    curr = LL.insert_node(i, curr)
ll.display()