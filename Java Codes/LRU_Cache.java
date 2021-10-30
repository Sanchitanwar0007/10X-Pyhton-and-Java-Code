import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class LRU_Cache {
    
    public static class LRU {
        class Node{
            int n,val;
            Node next,prev;
        }
        private void addafterhead(Node node){
            Node nn=head.next;
            node.next=nn;
            node.prev=head;
            head.next=node;
            nn.prev=node; 
        }
        private void removeNode(Node node){
            Node prvn=node.prev;
            Node nxtn=node.next;
            prvn.next=nxtn;
            nxtn.prev=prvn;
            node.next=node.prev=null;

        }
        private void moveToFront(Node node){
            removeNode(node);
            addafterhead(node);
        }
        HashMap<Integer,Node> map;
        int cap;
        Node head,tail;
        LRU(int capacity) {
            map = new HashMap<>();
            cap=capacity;
            head=new Node();
            tail= new Node();
            head.next=tail;
            tail.prev=head;
            head.prev=null;
            tail.next=null;
        }


        public int get(int key) {
            Node node= map.get(key);
            if(node==null){
                return -1;
            }else{
                int val=node.val;
                moveToFront(node);
                return val;
            }
        }

        public void put(int key, int value) {
            Node node= map.get(key);
            if(node==null){
                Node new_node= new Node();
                new_node.n=key;
                new_node.val=value;
                if(map.size()==cap){
                    Node lru_node=tail.prev;
                    map.remove(lru_node.n);
                    removeNode(lru_node);
                }
                map.put(key,new_node);
                addafterhead(new_node);
            }else{
                node.val=value;
                moveToFront(node);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        LRU obj = new LRU(Integer.parseInt(str.split(" ")[1]));

        while (true) {
            str = br.readLine();
            String inp[] = str.split(" ");
            if (inp.length == 1) {
                break;
            } else if (inp.length == 2) {
                System.out.println(obj.get(Integer.parseInt(inp[1])));
            } else if (inp.length == 3) {
                obj.put(Integer.parseInt(inp[1]), Integer.parseInt(inp[2]));
            }
        }
    }
}
