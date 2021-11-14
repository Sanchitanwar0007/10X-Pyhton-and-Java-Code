import java.util.*;
public class Check_arithmatic_Sequence {
    public static boolean is_airthmatic_sequence(int[] arr){
        if(arr.length==1){
            return true;
        }
        HashSet<Integer> set= new HashSet<>();
        int a=Integer.MAX_VALUE;
        int an=Integer.MIN_VALUE;

        for(int val:arr){
            a=Math.min(val,a);
            an=Math.max(val,an);
            set.add(val);
        }
        int d=(an-a)/(arr.length-1);
        for(int i=0;i<arr.length;i++){
            int ai=a+(i*d);
            if(!set.contains(ai)){
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int size=scan.nextInt();
        int arr[]= new int[size];
        for(int i=0;i<arr.length;i++){
            arr[i]=scan.nextInt();
        }
        System.out.print(is_airthmatic_sequence(arr));
        scan.close();
    }
}
