import java.util.*;
public class Sieve_of_erathonese {
    public static void Sieve_algo(int n){
        int m=(int)Math.sqrt(n)+1;
        boolean arr[]= new boolean[n+1];
        for(int i=0;i<n+1;i++){
            arr[i]=false;
        }
        for(int i=2;i<=m;i++){
            if(arr[i]==false){
                for(int j=i*i;j<n+1;j+=i){
                    arr[j]=true;
                }
            }
        }
        for(int i=0;i<arr.length;i++){
            if(arr[i]==false){
            System.out.print(i+" ");
        }
    }
    }
    public static void main(String[] args0){
        Scanner scan = new Scanner(System.in);
        int n=scan.nextInt();
        Sieve_algo(n);
        scan.close();
    }
}
