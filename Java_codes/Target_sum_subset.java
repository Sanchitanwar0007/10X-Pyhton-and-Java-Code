import java.util.*;
public class Target_sum_subset {
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int size=scan.nextInt();
        int arr[]= new int[size];
        for(int i=0;i<arr.length;i++){
            arr[i]=scan.nextInt();
        }
        int target=scan.nextInt();
        printTargetSubset(arr,0,"",0,target);
        scan.close();
    }
    public static void printTargetSubset(int arr[],int idx,String s,int ans,int target){
        if(idx==arr.length){
            if(ans==target){
                System.out.print(s+".");
            }
        return;
        }
        printTargetSubset(arr,idx+1,s+arr[idx]+",", ans+arr[idx], target);
        printTargetSubset(arr,idx+1,s, ans, target);
    }
}
