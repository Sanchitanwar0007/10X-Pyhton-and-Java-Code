import java.util.*;

//import BinaryTree_Constructor.Pair;
class BinaryTree{
    static class Node{
        int data;
        Node left;
        Node right;
        Node(int data,Node left,Node right){
            this.data=data;
            this.left=left;
            this.right=right;

        }
    }
    // Pair class for compairing
    public static class Pair{
        int state;
        Node node;
        Pair(int state,Node node){
            this.state=state;
            this.node=node;
        }
    }
    // Display tree data in pattern "left_node <- node_data -> right_node"
    public static void display(Node node){
        if(node==null){
            return;
        }
        String str="";
        str+=node.left==null?".":node.left.data+" ";
        str+="<-"+node.data+"->";
        str+=node.right==null?".":node.right.data+" ";
        System.out.println(str);
        display(node.left);
        display(node.right);

    }
    // Display data in preorder
    public static void preOrder(Node node){
        if(node==null){
            return;
        }
        System.out.print(node.data+" ");

        preOrder(node.left);

        preOrder(node.right);
        
    }
    //Display data in Inorder
    public static void InOrder(Node node){
        if(node==null){
            return;
        }
        InOrder(node.left);
        System.out.print(node.data+" ");
        InOrder(node.right);
        
    }
    //Display data in postOrder
    public static void postOrder(Node node){
        if(node==null){
            return;
        }
        postOrder(node.left);
        postOrder(node.right);
        System.out.print(node.data+" ");    
    }
    /*levelwise display tree 
           50
           /\
          /  \
         /    \
        25    75
        /\    /\
       12 37 62 87
           \  /
           30 70  
    The output must be 
    50
    25 75
    12 37 62 87
    30 70
           */
    public static void levelOrder(Node root){
        System.out.println();
        Queue<Node> mq= new ArrayDeque<>();
        mq.add(root);
        while(mq.size()>0){
            int count=mq.size();
            for(int i=0;i<count;i++){
                Node node= mq.remove();
                System.out.print(node.data+" ");
                if(node.left != null){
                    mq.add(node.left);
                }
                if(node.right != null){
                    mq.add(node.right);
                }
            }
            System.out.println();
        }
    }
    // NodeToRootpath in binarytree and if element found in binary tree then return true;
    public static boolean find(Node node,int data){
        if(node==null){
            return false;
        }
        if(node.data==data){
            return true;
        }
        boolean lc=find(node.left,data);
        if(lc){
            return true;
        }
        boolean rc=find(node.right,data);
        if(rc){
            return true;
        }
        return false;
    }
    public static ArrayList<Integer> nodeToRooPath(Node node, int data){
        if(node==null){
          return new ArrayList<>();
        }
        
        if(data==node.data){
            ArrayList<Integer> list= new ArrayList<>();
            list.add(node.data);
            return list;
        }
        ArrayList<Integer> lcList =nodeToRooPath(node.left, data);
        if(lcList.size()>0){
            lcList.add(node.data);
            return lcList;
        }
        ArrayList<Integer> rcList =nodeToRooPath(node.right, data);
        if(rcList.size()>0){
            rcList.add(node.data);
            return rcList;
        }
        return new ArrayList<>();
    }
    // Print k level down . In this prolem we have to print the kth level of binary tree and root level will be considere as 1st level
    public static void klevelDown(Node node,int k){
        if(node==null || k<0){
            return;
        }
        if(k==0){
            System.out.println(node.data);
        }
        klevelDown(node.left, k-1);
        klevelDown(node.right, k-1);
    }
    // Path To Leaf From Root In Range  .  In this problem we have to print the path to nide which lies in the range 
    public static void pathToLeafFromRoot(Node node, String path, int sum, int lo, int hi){
        if(node==null){
            return;
        }
        if(node.left==null && node.right==null){
            sum+=node.data;
            if(sum >= lo && sum<=hi){
                System.out.println(path+node.data+" ");
            }
        }
        
        pathToLeafFromRoot(node.left,path+node.data+" ",sum+node.data,lo,hi);
        pathToLeafFromRoot(node.right,path+node.data+" ",sum+node.data,lo,hi);

    }
//      Transform To Left-cloned Tree . In this question we are trying to add clone node of each node in the binary tree
    public static Node leftClonedTree(Node node){
        if(node==null){
            return null;

        }
        Node lcr=leftClonedTree(node.left);
        Node rcr=leftClonedTree(node.right);
        Node nn= new Node(node.data,lcr,null);
        node.left=nn;
        node.right=rcr;
        return node;
    }
    // Transform To Normal From Left-cloned Tree. Its the reverse of above solved quetion that is leftClonedTree
    public static Node normalTree(Node node){
        if(node==null){
            return null;
        }
        Node ln=normalTree(node.left.left);
        Node rn=normalTree(node.right);
         
        node.left=ln;
        node.right=rn;
        return node;
    }
    // Print Single child node . The nodes which have only single child node then we have to print them.
    public static void singleChild(Node node,Node parent){
        if(node==null){
            return;
        }
        if(parent != null && parent.left == node && parent.right== null){
            System.out.println(node.data);
        }else if(parent != null && parent.left==null && parent.right==node){
            System.out.println(node.data);
        }
        singleChild(node.left,node);
        singleChild(node.right,node);
    }
    //Removes leaf Node from binary tree which contains null in left and right 
    public static Node removeLeafNode(Node node){
        if(node==null)
        {
            return null;
        }
        if(node.left==null && node.right==null){
            return null;
        }
        node.left=removeLeafNode(node.left);
        node.right=removeLeafNode(node.right);
        return node;
    }
    // Diameter of a binary tree. Two approaches are used for solving 
    public static int height(Node node){
        if(node==null){
            return -1;
        }
        int lh= height(node.left);
        int rh= height(node.right);
        int ht=Math.max(lh,rh)+1;
        return ht;
    }
    // This method use O(N^2) for finding diameter of given problem this can be done in O(N) and next method is use for same in O(N)
    public static int Diameter(Node node){
        if(node==null){
            return 0;
        }
        int ld=Diameter(node.left);
        int rd=Diameter(node.right);
        int f=height(node.left)+height(node.right)+2;
        int dia=Math.max(f,Math.max(ld,rd));
        return dia;
    }
    // Finding Diameter of binary tree in O(N)\
    static class DiaPair{
        int ht;
        int dia;
    }
    public static DiaPair Diameter2(Node node){
        if(node==null){
            DiaPair ndp=new DiaPair();
            ndp.ht=-1;
            ndp.dia=0;
            return ndp;
        }
        DiaPair ldp=Diameter2(node.left);
        DiaPair rdp= Diameter2(node.right);
        DiaPair mp= new DiaPair();
        mp.ht=Math.max(ldp.ht,rdp.ht)+1;
        int fes=ldp.ht+rdp.ht+2;
        mp.dia=Math.max(fes,Math.max(ldp.dia,rdp.dia));
        return mp;
    }
    //Tilt of binary tree . The tilt of root node is diffence of sum of all left nodes and sum of right nodes. Siilary tilt of every node is determined
    static int tilt=0;
    public static int tilt(Node node){
        if(node==null){
            return 0;
        }
        int ls=tilt(node.left);
        int rs=tilt(node.right);
        tilt+=Math.abs(ls-rs);
        int sum=ls+rs+node.data;
        return sum;
    }
    // isBST :- in this problem we detect that wether the given binary tree is Binary Search tree or not.

   static class BSTPair{
       boolean isbst;
       int min;
       int max;

   }
   public static BSTPair isBST(Node node){
       if(node==null){
           BSTPair bp= new BSTPair();
           bp.isbst=true;
           bp.min=Integer.MAX_VALUE;
           bp.max=Integer.MIN_VALUE;
           return bp;
       }

        BSTPair lp=isBST(node.left);
        BSTPair rp=isBST(node.right);
        BSTPair mp= new BSTPair();
        mp.isbst=lp.isbst && rp.isbst && (node.data >=lp.max && node.data<=rp.min);
        mp.min=Math.min(node.data,Math.min(lp.min,rp.min));
        mp.max=Math.max(node.data,Math.max(rp.max,lp.max));
        return mp;

   }
   // isBalanced Tree : By Chain rule : Balance tre is if the difference between the height of left tree and right tree is less than equal to 1 otherwise tree is not balanced
   static boolean isBal=true;
   public static int isBalanced(Node node){
       if(node==null)
       {
           return 0;
       }
       int lh=isBalanced(node.left);
       int rh=isBalanced(node.right);
       if(Math.abs(lh-rh)>1){
           isBal=false;
       }
       int ht=Math.max(lh,rh)+1;
       return ht;
    }
    // isBalanced Tree approch is also solved by Pair method
    static class balPair{
        boolean isbal;
        int ht;

    }
    public static balPair isBal(Node node){
        if(node==null){
            balPair bp=new balPair();
            bp.isbal=true;
            bp.ht=0;
            return bp;
        }
        balPair bl=isBal(node.left);
        balPair br=isBal(node.right);
        balPair mp= new balPair();
        mp.isbal=bl.isbal && br.isbal && Math.abs((bl.ht-br.ht))<=1;
        mp.ht=Math.max(bl.ht,br.ht)+1;
        return mp;

    }
    public static void main(String args[]){
       // Integer arr[]={4,2,9,3,5,null,7};
        Integer arr[]= {50,25,12,null,null,37,30,null,null,null,75,62,null,70,null,null,87,null,null};
        Stack<Pair> st= new Stack<>();
        Node root=new Node(arr[0],null,null);
        Pair rnp= new Pair(1,root);
        st.push(rnp);
        int index=0;
        while(st.size()>0){
            Pair rp=st.peek();
            if(rp.state==1){
             index++;
             if(arr[index]!=null){
                Node ln=new Node(arr[index],null,null);
                rp.node.left=ln;
                Pair lp=new Pair(1,ln);
                st.push(lp);

             }else{
                rp.node.left=null;
             }
             rp.state++;
            }else if(rp.state==2){
                index++;
                if(arr[index]!=null){
                   Node rn=new Node(arr[index],null,null);
                   rp.node.right=rn;
                  Pair rightp=new Pair(1,rn);
                   st.push(rightp);
   
                }else{
                   rp.node.right=null;
                }
                rp.state++;
            }else{
                st.pop();
            }   
        }
        display(root);
        preOrder(root);
        System.out.println();

        InOrder(root);
        System.out.println();
        postOrder(root);
        levelOrder(root);
        // boolean b=find(root,90);
        System.out.println("NodeToRootPath is:->"+nodeToRooPath(root,30));
        klevelDown(root, 3);
        pathToLeafFromRoot(root,"",0,50,900);
        leftClonedTree(root);
        System.out.println("Transform To Left-cloned Tree");
        
        display(root);
        System.out.println("Transform To normal Tree");
        normalTree(root);
        display(root);
        System.out.println("Single child node are:");
        singleChild(root,null);
        removeLeafNode(root);
        System.out.println("After removing leaf nodes firm binary tree");
        display(root);
        System.out.print(height(root));
        System.out.println();
        System.out.println("Diameter of binary tree is : "+Diameter(root));
        DiaPair nn=Diameter2(root);
        System.out.println("Diameter in O(N) is : "+nn.dia);
        tilt(root);
        System.out.println("Tilt of binary tree is : "+tilt);
        BSTPair bst= isBST(root);
        System.out.println(bst.isbst);
        isBalanced(root);
        System.out.println(isBal);
        balPair bal= isBal(root);
        System.out.println(bal.isbal);

    }
}