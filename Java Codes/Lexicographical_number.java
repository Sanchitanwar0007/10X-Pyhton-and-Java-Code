import java.util.*;
public class Lexicographical_number {
    public static void main(String[] args) {
        Scanner scan= new Scanner(System.in);
        int n= scan.nextInt();
        for(int i=1;i<=9;i++){
            lexicography(i,n);
        }
        scan.close();
    }
    public static void lexicography(int i, int n){
        if(i>n){
            return;
        }
        System.out.println(i);
        for(int j=0;j<10;j++){
            lexicography(10*i+j, n);
        }
    }
}
