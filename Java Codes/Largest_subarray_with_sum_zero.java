import java.util.*;
public class Largest_subarray_with_sum_zero {
    public static void main(String args[]){
        Scanner scan= new Scanner(System.in);
        int n=scan.nextInt();
        int arr[]= new int[n];
        for(int i=0;i<n;i++){
            arr[i]=scan.nextInt();
        }
        HashMap<Integer,Integer> map= new HashMap<>();
        int sum=0;
        map.put(0,-1);
        int max=0;
        for(int i=0;i<arr.length;i++){
            sum+=arr[i];
            if(map.containsKey(sum)){
                int temp=i-map.get(sum);
                if(temp>max){
                    max=temp;
                }
            }else{
                map.put(sum,i);
            }
        }
        System.out.print(map);
        System.out.print(max);
        scan.close();
    }
}
