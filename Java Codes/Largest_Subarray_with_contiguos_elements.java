import java.util.*;
public class Largest_Subarray_with_contiguos_elements {
    public static int large_subarray(int arr[]){
        int ans=0;
        for(int i=0;i<arr.length-1;i++){
            int min=arr[i];
            int max=arr[i];
            HashSet<Integer> set= new HashSet<>();
            set.add(arr[i]);
            for(int j=i+1;j<arr.length;j++){
                min=Math.min(min,arr[j]);
                max=Math.max(max,arr[j]);
                if(set.contains(arr[j])){
                    break;
                }
                set.add(arr[j]);
                if(max-min==j-i){
                    int length=j-i+1;
                    if(length>ans){
                        ans=length;
                    }
                }
            }
        }
        // System.out.print(ans);
        return ans;
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int size=scan.nextInt();
        int arr[]= new int[size];
        for(int i=0;i<size;i++){
            arr[i]=scan.nextInt();
        }
        System.out.print("Largest Subarray of length is : "+large_subarray(arr));
        scan.close();
    }
}
