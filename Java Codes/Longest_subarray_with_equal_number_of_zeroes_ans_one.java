import java.util.*;
public class Longest_subarray_with_equal_number_of_zeroes_ans_one {
    public static int equal_0_1(int[] arr){
        int ans=0;
        HashMap<Integer,Integer> map= new HashMap<>();
        map.put(0,-1);
        int sum=0;
        for(int i=0;i<arr.length;i++){
            if(arr[i]==0){
                sum-=1;
            }else{
                sum+=1;
            }
            if(map.containsKey(sum)){
                int temp=i-map.get(sum);
                ans=Math.max(ans,temp);
            }else{
                map.put(sum,i);
            }
        }

        return ans;
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int size=scan.nextInt();
        int arr[]= new int[size];
        for(int i=0;i<size;i++){
            arr[i]=scan.nextInt();
        }
        System.out.print(equal_0_1(arr));
        scan.close();
    }
}
