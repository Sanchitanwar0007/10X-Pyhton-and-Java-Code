import java.util.*;
public class Longest_Consecutive_sequence {
    public static void main(String[] args){
        Scanner scan=new Scanner(System.in);
        int n=scan.nextInt();
        int arr[]=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=scan.nextInt();
        }
        HashMap<Integer,Boolean> map=new HashMap<>();
        for(int val:arr){
            map.put(val,true);
        }
        for(int val:arr){
            if(map.containsKey(val-1)){
                map.put(val,false);
            }
        }
        int max=0;
        int starting_point=0;
        for(int val:arr){
            if(map.get(val)==true){
                int tl=0;
                int tsp=val;
                while(map.containsKey(val+tl)){
                    tl++;
                }
                if(tl>max){
                    max=tl;
                    starting_point=tsp;
                }
            }
        }
        // System.out.println(max+"  "+starting_point);
        for(int i=0;i<max;i++){
            System.out.println(starting_point+i);
        }
        scan.close();
    }
}
