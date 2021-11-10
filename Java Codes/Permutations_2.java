import java.util.*;
public class Permutations_2 {
    public static void main(String[] args) {
        Scanner scan= new Scanner(System.in);
        int n=scan.nextInt();
        int r=scan.nextInt();
        permute(1,n,new int[r],0,r,"");
        scan.close();
    }
    public static void permute(int target,int n,int arr[],int slen,int r,String ans){
        if(target>n){
            if(slen==r){
                System.out.println(ans);
            }
            return;
        }
        for(int i=0;i<r;i++){
            if(arr[i]==0){
                arr[i]=1;
                permute(target+1, n, arr, slen+1, r, ans+(i+1));
                arr[i]=0;
            }
        }
        permute(target+1, n, arr, slen, r, ans+0);
    }
}
