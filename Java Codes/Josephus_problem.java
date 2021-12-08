import java.util.*;
public class Josephus_problem {
    public static int josep_problem(int n,int k){
        if(n==1){
            return 0;

        }
        int rem=josep_problem(n-1, k);
        int y=(rem + k) % n;
        return y;
    }
    public static void main(String[] args) {
        Scanner scan= new Scanner(System.in);
        int n=scan.nextInt();
        int k=scan.nextInt();
        System.out.println(josep_problem(n,k));
        scan.close();
    }
}
