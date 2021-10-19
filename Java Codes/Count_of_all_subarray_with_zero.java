import java.util.*;
public class Count_of_all_subarray_with_zero {
    public static void main(String args[]){
        Scanner scan= new Scanner(System.in);
        int n=scan.nextInt();
        int arr[]= new int[n];
        for(int i=0;i<n;i++){
            arr[i]=scan.nextInt();
        }
        HashMap<Integer,Integer> map= new HashMap<>();
        map.put(0,1);
        int sum=0;
        int count=0;
        for(int i=0;i<n;i++){
            sum+=arr[i];
            if(map.containsKey(sum)){
                count+=map.get(sum);
                map.put(sum,map.get(sum)+1);
            }else{
                map.put(sum,1);
            }
        }
        System.out.print(count);
        scan.close();
        }
}
