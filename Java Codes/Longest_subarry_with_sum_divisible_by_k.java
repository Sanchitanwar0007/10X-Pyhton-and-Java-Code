import java.util.*;
public class Longest_subarry_with_sum_divisible_by_k {
    public static int longest_subarray(int nums[],int k){
        HashMap<Integer,Integer> map= new HashMap<>();
        map.put(0,-1);
        int sum=0;
        int ans=0;
        for(int i=0;i<nums.length;i++){
            sum+=nums[i];
            int rem=sum%k;
            if(rem<0){
                rem+=k;
            }
            if(map.containsKey(rem)){
              int temp=i-map.get(rem);
                if(temp>ans){
                    ans=temp;
                }
            }else{
                map.put(rem,i);
            }
            
        }
        return ans;
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int size=scan.nextInt();
        int arr[]= new int[size];
        for(int i=0;i<arr.length;i++){
            arr[i]=scan.nextInt();
        }
        int k=scan.nextInt();
        System.out.print(longest_subarray(arr, k));
        scan.close();
    }
}
