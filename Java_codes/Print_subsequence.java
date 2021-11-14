import java.util.*;
public class Print_subsequence{
   public static void main(String[] args){
       Scanner scan= new Scanner(System.in);
        String str=scan.next();
        ArrayList<String> list= new ArrayList<>();
        print_sub_sequence(str,"",list);
        System.out.print(list);
        scan.close();
   }
   public static void print_sub_sequence(String str,String ans,ArrayList<String> list){
    if(str.length()==0){
        list.add(ans);
        System.out.print(ans+" ");
        return;
    }
    char ch=str.charAt(0);
    String ros=str.substring(1);
    print_sub_sequence(ros,ans+ch,list);
    print_sub_sequence(ros,ans+"",list);
   }
}
