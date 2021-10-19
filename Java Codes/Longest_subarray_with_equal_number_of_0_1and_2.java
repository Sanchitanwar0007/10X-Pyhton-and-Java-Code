import java.util.*;
public class Longest_subarray_with_equal_number_of_0_1and_2 {
    public static int longest_0_1_2(int arr[]){
        HashMap<String,Integer> map= new HashMap<>();
        int c0=0;
        int c1=0;
        int c2=0;
        int ans=0;
        String key=(c2-c1)+"#"+(c1-c0);
        map.put(key,-1);
        for(int i=0;i<arr.length;i++){
            if(arr[i]==0){
                c0++;
            }else if(arr[i]==1){
                c1++;
            }else{
                c2++;
            }
            key=(c2-c1)+"#"+(c1-c0);
            if(map.containsKey(key)){
                ans=Math.max(ans,i-map.get(key));
            }else{
                map.put(key,i);
            }

        }
        return ans;
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int size=scan.nextInt();
        int arr[]=new int[size];
        for(int i=0;i<arr.length;i++){
            arr[i]=scan.nextInt();
        }
        System.out.print(longest_0_1_2(arr));
        scan.close();
    }
}
