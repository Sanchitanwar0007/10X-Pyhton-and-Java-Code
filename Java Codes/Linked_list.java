class Node{
    int data;
    Node next;
    Node(int data,Node next){
        this.data=data;
        this.next=next;
    }
}
public class Linked_list {
    public static Node make_linked_list(){
        Node node1=new Node(12,null);
        Node head=node1;
        Node node2=new Node(24,null);
        head.next=node2;
        Node node3=new Node(36,null);
        node2.next=node3;
        Node node4=new Node(48,null);
        node3.next=node4;
        return head;
    }
    public static Node insert_at_head(Node head,int data){
        Node new_node=new Node(data,null);
        if(head==null){
            head=new_node;
            return head;
        }
        new_node.next=head;
        head=new_node;
        return head;
    }
    public static void insert_at_end(Node head,int data){
        Node new_node=new Node(data,null);
        if(head==null){
            head=new_node;
            return;
        }
        Node curr=head;
        while(curr.next!=null){
            curr=curr.next;
        }
        curr.next=new_node;
        
    }
    public static int size(Node head){
        Node curr=head;
        int size=0;
        while(curr!=null){
            size++;
            curr=curr.next;
        }
        return size;
    }
    public static Node insert_at(Node head,int pos,int data){
        int size=size(head);
        // System.out.println(size);
        Node new_node=new Node(data,null);
        if(pos>size){
            System.out.print("Position is not found");
            return head;
        }
        if(pos==0){
            new_node.next=head;
            
            return new_node;
        }
        Node curr=head;
        int s=1;
        while(s!=pos){
            s++;
            curr=curr.next;
        }
        Node temp=curr.next;
        curr.next=new_node;
        new_node.next=temp;
        return head;
    }
    public static int mid_ll(Node head){
        if(head==null){
            return 0;
        }
        if(head.next==null){
            return head.data;
        }
        Node slow=head;
        Node fast=head;
        while(fast!=null && fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;
        }
        return slow.data;
    }
    public static Node reverse_ll(Node head){
        if(head==null || head.next==null){
            return head;
        }
        Node curr=head;
        Node forw=null;
        Node prev=null;
        while(curr!=null){
            forw=curr.next;
            curr.next=prev;
            prev=curr;
            curr=forw;
        }
        head=prev;
        return head;
    }
    public static void Display(Node head){
        Node curr=head;
        while(curr!=null){
            if(curr.next==null){
                System.out.print(curr.data);
                curr=curr.next;
                continue;
            }
            System.out.print(curr.data+"->");
            curr=curr.next;
        }
    }
    public static void main(String[] args) {
        // Node head=make_linked_list();

        Node head=null;
        head=insert_at_head(head,12);
        head=insert_at_head(head,25);
        head=insert_at_head(head,26);
        // head=insert_at_head(head,45);
        insert_at_end(head,100);
        insert_at_end(head, 102);
        head=insert_at(head,5,42);
        head=insert_at(head,0,4);
        head=insert_at(head,3,89);
        Display(head);
        System.out.println();
        head=reverse_ll(head);

        Display(head);
        System.out.println(mid_ll(head));
    }
}
