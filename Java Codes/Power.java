import java.util.*;
public class Power {
    public static int pow(int n,int x){
        if(x==0){
            return 1;
        }
        
        int nb2=pow(n,x/2);
        int fans=nb2*nb2;
        if(x%2==1){
            fans=fans*n;
        }
        return fans;
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int n=scan.nextInt();
        int x=scan.nextInt();
        System.out.print(pow(n,x));
        scan.close();
    }   
}
