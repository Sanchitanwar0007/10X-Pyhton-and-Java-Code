import java.util.*;
public class Print_encoding {
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        String str=scan.next();
        print_encoding(str,"");
        scan.close();

    }
    public static void print_encoding(String str,String ans){
        if(str.length()==0){
            // System.out.print(ans+" ");
            return;
        }else if(str.length()==1){
            char ch=str.charAt(0);
            if(ch=='0'){
                return;
            }else{
                System.out.print((ans+(char)(ch+48))+" ");
                return;
            }
        }else{
            char ch=str.charAt(0);
            String ros=str.substring(1);
            if(ch=='0'){
                return;
            }else{
                print_encoding(ros, ans+(char)(ch+48));
            }
            String ch12=str.substring(0,2);
            String ros12=str.substring(2);
            int limit=Integer.parseInt(ch12);
            if(limit<=26){
                print_encoding(ros12, ans+(char)(Integer.parseInt(ch12)+96));
            }
        }

        
    }
        
    }

