import java.util.*;
public class Double_pair_array {
    public static boolean is_double_pair(int arr[]){

        Integer ar[]= new Integer[arr.length];
        for(int i=0;i<arr.length;i++){
            ar[i]=arr[i];
        }
        HashMap<Integer,Integer> map= new HashMap<>();
        for(int val:arr){
            map.put(val,map.getOrDefault(val,0)+1);
        }
        Arrays.sort(ar,(a,b)->{
            return Math.abs(a)-Math.abs(b);
        });
        for(Integer val:ar){
            if(map.get(val)==0){
                continue;
            }
            if(map.containsKey(2*val) && map.get(2*val)!=0){
                map.put(val,map.get(val)-1);
                map.put(2*val,map.get(2*val)-1);
            }else{
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int size=scan.nextInt();
        int arr[]=new int[size];
        for(int i=0;i<arr.length;i++){
            arr[i]=scan.nextInt();
        }
        System.out.print(is_double_pair(arr));
        scan.close();
    }
}
