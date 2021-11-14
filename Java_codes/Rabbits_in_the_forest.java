import java.util.*;
public class Rabbits_in_the_forest {
    public static int minimum_rabbits(int arr[]){
        HashMap<Integer,Integer> map= new HashMap<>();
        for(int var:arr){
            map.put(var,map.getOrDefault(var,0)+1);
        }
        int ans=0;
        for(int key:map.keySet()){
            int rabbits=key+1;
            int sam_rabbit=map.get(key);
            int group=(int)Math.ceil(sam_rabbit*1.0/rabbits*1.0)*rabbits;
            ans+=group;
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
        System.out.print(minimum_rabbits(arr));
        scan.close();
    }
}
