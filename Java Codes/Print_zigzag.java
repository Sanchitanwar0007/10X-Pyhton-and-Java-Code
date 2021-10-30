import java.util.*;
public class Print_zigzag {
    public static void zig_zag(int n){
        if(n==0){
            return;
        }
        System.out.print(n+" ");
        zig_zag(n-1);
        System.out.print(n+" ");
        zig_zag(n-1);
        System.out.print(n+" ");
        
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int n=scan.nextInt();
        zig_zag(n);
        scan.close();
    }
}
