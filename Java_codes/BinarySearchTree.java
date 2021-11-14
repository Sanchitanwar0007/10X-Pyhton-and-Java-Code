public class BinarySearchTree {
   public static class Node{
                Node left;
                Node right;
                int data;
                Node(int data,Node left,Node right){
                    this.data=data;
                    this.left=left;
                    this.right=right; 
                }
    }

    public static Node construct(int arr[],int lo, int hi){
            if(lo>hi){
                 return null;
            }
            int mid=(lo+hi)/2;
            int data=arr[mid];
            Node lc=construct(arr,lo,mid-1);
            Node rc=construct(arr,mid+1,hi);
            Node n=new Node(data,lc,rc);
            return n;
        }
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
        // Size of BST is returned
  public static int size(Node node){
      if(node==null){
          return 0;
      }
      int ls=size(node.left);
      int rs=size(node.right);
      int size=ls+rs+1;
      return size;
  }
  public static int sum(Node node){
      if(node==null){
          return 0;
      }
      int ls=sum(node.left);
      int rs=sum(node.right);
      int sum=ls+rs+node.data;
      return sum;
  }
  public static int max(Node node){
      if(node.right!=null){
          return max(node.right);
      }else{
      return node.data;
      }

  } 
  public static int min(Node node){
      if(node.left!=null){
          return min(node.left);

      }
      else{
          return node.data;
      }
  }
  public static boolean find(Node node,int data){
    if(node==null){
        return false;
    }
    if(node.data>data){
        return find(node.left,data);
    }else if(node.data<data){
        return find(node.right,data);
    
    }else{
        return true;
    }

  }
//   Add node to BST
  public static Node add(Node node, int data) {
    if(node==null){
        return new Node(data,null,null);
    }
    if(data>node.data){
        node.right=add(node.right,data);
    }else if(data<node.data){
        node.left=add(node.left,data);
    }
    return node;
  }
public static void main(String[] args) throws Exception{
    int arr[]={12,15,17,19,22,28,89};
    int data=28;
    Node root=construct(arr,0,arr.length-1);
    display(root);
    System.out.println("Size of BST is =>"+size(root));
    System.out.println("Total Sum of BST is =>"+sum(root));
    System.out.println("Max in BST is =>"+max(root));
    System.out.println("Min in BST is =>"+min(root));
    System.out.println("Is given Element "+data+" is present in tree=> " +find(root,data));
    add(root,87);
    display((root));
}
}
    

