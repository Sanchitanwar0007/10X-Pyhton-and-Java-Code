import java.util.*;
public class Tower_of_hanoi {
    public static void toh(int n,int a,int b,int c){
        if(n==0){
            return;
        }
        toh(n-1,a,c,b);
        System.out.println(n+"["+a+"->"+b+"]");
        toh(n-1,c,b,a);
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int n=scan.nextInt();
        int a=scan.nextInt();
        int b=scan.nextInt();
        int c=scan.nextInt();
        toh(n,a,b,c);
    }
}
