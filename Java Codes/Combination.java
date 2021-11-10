import java.util.*;
public class Combination {
    public static void main(String[] args) {
        Scanner scan= new Scanner(System.in);
        int n=scan.nextInt();
        int r=scan.nextInt();
        combinations(n, r, "", 1,0);
        scan.close();
    }
    public static void combinations(int n,int r,String ans,int target,int i){
        if(target>n){
            if(i==r)
            System.out.println(ans);
            return;
        }
        combinations(n, r, ans+"i", target+1,i+1);
        combinations(n, r, ans+"-", target+1,i);
    }
}
