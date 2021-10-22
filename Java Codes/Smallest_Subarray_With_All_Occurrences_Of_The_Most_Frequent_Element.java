import java.util.*;
public class Smallest_Subarray_With_All_Occurrences_Of_The_Most_Frequent_Element {
    public static void answer(int[] arr){
        HashMap<Integer,Integer> map= new HashMap<>();
        HashMap<Integer,Integer> i_map= new HashMap<>();
        int hfreq=0;
        int start=0;
        int end=0;
        int len=end-start+1;
        for(int i=0;i<arr.length;i++){
            if(map.containsKey(arr[i])){
                map.put(arr[i],map.get(arr[i])+1);
            }else{
                map.put(arr[i],1);
                i_map.put(arr[i],i);
            }
            if(map.get(arr[i])>hfreq){
                hfreq=map.get(arr[i]);
                start=i_map.get(arr[i]);
                end=i;
                len=end-start+1;
            }else if(map.get(arr[i])==hfreq){
                int temp=i-i_map.get(arr[i])+1;
                if(temp<len){
                    len=temp;
                    start=i_map.get(arr[i]);
                    end=i;
                }
            }
        }
        System.out.println(arr[start]);
        System.out.println(start);
        System.out.print(end);
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int size=scan.nextInt();
        int arr[]= new int[size];
        for(int i=0;i<size;i++){
            arr[i]=scan.nextInt();
        }
        answer(arr);
        scan.close();
    }
}
