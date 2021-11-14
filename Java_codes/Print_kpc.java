import java.util.*;
public class Print_kpc {
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        String str=scan.next();
        printKPC(str,"");
        scan.close();
    }
    static String[] arr={"","abc","def","ghi","jkl","mno","pqrs","tu","vwx","yz"};
    public static void printKPC(String str,String ans){
        if(str.length()==0){
            System.out.print(ans+" ");
            return;
        }
        char ch=str.charAt(0);
        String rs=str.substring(1);
        for(int i=0;i<arr[ch-48].length();i++){
            char ch2=arr[ch-48].charAt(i);
            printKPC(rs, ans+ch2);
        }
    }
}
