import java.util.*;
public class Count_of_subarrays_having_sum_equals_to_k {
    public static int count_subarrays(int[] arr,int target){
        int ans=0;
        HashMap<Integer,Integer> map= new HashMap<>();
        map.put(0,1);
        int sum=0;
        for(int i=0;i<arr.length;i++){
            sum+=arr[i];
            if(map.containsKey(sum-target)){
                ans+=map.get(sum-target);
            }
            map.put(sum,map.getOrDefault(sum,0)+1);
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
        int target=scan.nextInt();
        System.out.print(count_subarrays(arr,target));
        scan.close();
    }
}
