class Node{
    int data;
    Node next;
    Node(int data,Node next){
        this.data=data;
        this.next=next;
    }
}
public class Linkerd_list {
    public static Node linked_list(){
        Node head=null;
        Node node1= new Node(12,null);
        head=node1;
        Node node2=new Node(24,null);
        head.next=node2;
        Node node3 = new Node(25,null);
        node2.next=node3;
        Node node4= new Node(26,null);
        node3.next=node4;
        
        return head;
    }
    public static Node insert_at_head(Node head,Node new_node){
        if(head==null){
            head=new_node;
            return head;
        }
        new_node.next=head;
        head=new_node;
        return head;
    }
    public static void display(Node head){
        Node temp=head;
        while(temp!=null){
            System.out.print(temp.data+"->");
            temp=temp.next;
        }
        System.out.println("null");
    }
    public static void insert_in_between(Node head,int pos,Node newNode){
        int count=1;
        Node temp=head;
        while(count!=pos){
            count++;
            try{
            temp=temp.next;
        }catch(NullPointerException e){
            System.out.println("You are inserting at out of length position");
            e.printStackTrace();
            return;
        }
    }
    try{
        newNode.next=temp.next;
        temp.next=newNode;
    }catch(NullPointerException e){
        System.out.println("You are inserting at out of length position");
            e.printStackTrace();
            return;
    }
        
}
    public static void main(String args[]){
        Node head=linked_list();
        display(head);
        Node new_node=new Node(40,null);
        head=insert_at_head(head, new_node);
        Node new_node2=new Node(50,null);
        insert_in_between(head,1,new_node2);
        display(head);
    }
}
