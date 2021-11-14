import java.util.*;
public class Permutation_1 {
    public static void main(String[] args) {
        Scanner scan= new Scanner(System.in);
        int n=scan.nextInt();
        int r=scan.nextInt();
        int arr[]=new int[n];
        permute(arr,n,r,1);
        scan.close();
    }
    public static void permute(int arr[],int n,int r,int target)
    {
        if(target>r){
            for(int i=0;i<arr.length;i++){
                System.out.print(arr[i]);
            }
            System.out.println();
            return;
        }
        for(int i=0;i<n;i++){
            if(arr[i]==0){
                arr[i]=target;
                permute(arr, n, r, target+1);
                arr[i]=0;
            }
        }
    }
}
