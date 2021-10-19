class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    @staticmethod
    def insert_node(val, current):
        temp = Node(val)
        current.next = temp
        current = current.next
        return current

    #complete the function given below
    @staticmethod
    def Negativity(List):
        neg=0
        ll_size=0
        temp=List.head
        while(temp!=None):
            if(temp.data<0):
                neg+=1
            ll_size+=1
            temp=temp.next
        # print(neg,ll_size)
        ret=int((neg/ll_size)*100)
        return ret

ll = LL()
num = [int(i) for i in input().split("->")]
ll.head = Node(num[0])
curr = ll.head
for i in num[1:]:
    curr = LL.insert_node(i, curr)
print(LL.Negativity(ll))