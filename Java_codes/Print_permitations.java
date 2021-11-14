import java.util.*;
public class Print_permitations {
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        String str=scan.next();
        permutation(str,"");
        scan.close();

    }
    public static void permutation(String str,String ans){
        if(str.length()==0){
            System.out.print(ans+" ");
            return;
        }

        for(int i=0;i<str.length();i++){
            char ch=str.charAt(i);
            String ros=str.substring(0,i)+str.substring(i+1);
            permutation(ros, ans+ch);
        }
    }
}
