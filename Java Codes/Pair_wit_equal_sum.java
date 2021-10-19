import java.util.*;
public class Pair_wit_equal_sum {
    public static boolean pair(int arr[]){
        HashSet<Integer> set= new HashSet<>();
        for(int i=0;i<arr.length;i++){
            for(int j=i+1;j<arr.length;j++){
                int temp=arr[i]+arr[j];
                if(set.contains(temp)){
                    return true;
                }else{
                    set.add(temp);
                }
            }
        }
        return false;
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int size=scan.nextInt();
        int arr[]= new int[size];
        for(int i=0;i<arr.length;i++){
            arr[i]=scan.nextInt();
        }
        System.out.print(pair(arr));
        scan.close();
    }
}
